import numpy as np
import pandas as pd
import gspread as gs
from fuzzywuzzy import fuzz


class TopicPriorityTag():

	TOPIC_KEYWORDS_LOOKUP = {}
	TOPIC_KEYWORDS_PRIORITY_LOOKUP = {}


	def __init__(self):
		# read keyword topic matrix
		gc = gs.service_account(filename='../creds/service_account.json')
		sheets_url = "https://docs.google.com/spreadsheets/d/1nksszctHCK_Q9NiMNuVwkCPLmu4TsciV7fg6zTSmIsg"
		sh = gc.open_by_url(sheets_url)
		ws = sh.worksheet('Table')
		table_df = pd.DataFrame(ws.get_all_records())
		table_df['keywords'] = table_df['Model Keywords'].apply(lambda x: [c.strip() for c in x.split(',') if len(c)>0])\
		                      + table_df['Citizen Charter Keywords'].apply(lambda x: [c.strip() for c in x.split(',') if len(c)>0])
		topic_keywords_df = table_df.groupby('Category').agg({'Priority': 'mean', 'keywords': 'sum'})
		self.TOPIC_KEYWORDS_LOOKUP =  topic_keywords_df['keywords'].to_dict()
		self.TOPIC_KEYWORDS_PRIORITY_LOOKUP = topic_keywords_df['Priority'].astype(int).to_dict()

	def get_topic_keyword_lookup_dict(self):
		return self.TOPIC_KEYWORDS_LOOKUP


	def compute_fuzz_score(self, word1,word2, show_words=False):
	    if show_words:
	        print(word1,word2)
	    return fuzz.token_sort_ratio(word1, word2)

	def tag_topic_category(self, text, print_word_match=False):
	    text = text.split(' ')
	    topic_category = []
	    for category in self.TOPIC_KEYWORDS_LOOKUP .keys():
	        keywords = self.TOPIC_KEYWORDS_LOOKUP[category]
	        match_scores = [self.compute_fuzz_score(word,keyword) if len(word)>8 else 100*(word==keyword) for word in text for keyword in keywords]
	        if any([score > 75 for score in match_scores]):
	            topic_category.append(category)
	            if print_word_match:
	                match_scores = np.reshape(match_scores, (len(text),len(keywords))).max(axis=1)
	                print('Category '+category+' matched on words: '+str([text[i] for i,score in enumerate(match_scores) if score >75 ]) )
	    return topic_category

	def tag_topic_priority(self, topic_categories):
	    try:
	        return np.max([self.TOPIC_KEYWORDS_PRIORITY_LOOKUP[k] for k in topic_categories])
	    except:
	        return 0