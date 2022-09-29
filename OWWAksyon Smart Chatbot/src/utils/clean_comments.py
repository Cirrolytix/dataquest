import numpy as np
import pandas as pd
from re import sub

from nltk.corpus import stopwords
from fuzzywuzzy import fuzz
import itertools



class CommentCleaner:
	STOPWORDS = []
	PADWORDS = []

	def __init__(self):
		#load stopwords
		stopwords_en = stopwords.words('english')
		stopwords_tl_df = pd.read_csv('../data/tl_stopwords.csv', header=None)
		stopwords_tl = [s for s in stopwords_tl_df[0].values if len(s)]
		self.STOPWORDS.extend(stopwords_en)
		self.STOPWORDS.extend(stopwords_tl)

		padwords_df = pd.read_csv('../data/owwa_comments_padwords.csv', header=None)
		padwords_init = [s for s in padwords_df[0].values]
		self.PADWORDS.extend(padwords_init)
		#for padword in padwords_init:
		#	if len(padword)>5:
		#		self.PADWORDS.extend(self.generate_forms(padword))

	def get_stopwords(self):
		return self.STOPWORDS

	def get_padwords(self):
		return self.PADWORDS

	def censor_name(self,name):
		first_name = name.split(' ')[0] 
		return first_name + " ***********"

	def censor_text(self,text):
		return sub(r'\d{5,15}', '*******', text)

	def remove_stopwords(self, comment_text):
	    text = comment_text.split(' ')
	    filtered_text = [word for word in text if word not in self.STOPWORDS]
	    return ' '.join(filtered_text)

	def remove_padwords(self, text):
	    text = text.split(' ')
	    match_scores = [self.compute_fuzz_score(word,padword) for word in text for padword in self.PADWORDS]
	    match_scores = np.reshape(match_scores, (len(text),len(self.PADWORDS))).max(axis=1)
	    filtered_text = [word for i,word in enumerate(text) if match_scores[i] <= 65]
	    return ' '.join(filtered_text)

	def sanitize_text(self, comment_text):
		# replace punctuation by space
	    text = sub(r'(?:_|[^\s\w])(?!(?<=\d\.)\d)', " ", comment_text)
	    # remove extra spaces, and
	    # non-alphabetical characters excluding periods
	    #remove numbers longer than 4 
	    text = sub(r'\d{5,15}', '', text)

	    # remove one letter words
	    text = ' '.join([t for t in text.split() if len(t)>2])
	    # lower case
	    text = text.lower()
	    return text

	def clean_comment(self, comment_text):
	    # replace punctuation by space
	    text = self.sanitize_text(comment_text)
	    # remove stopwords
	    text = self.remove_stopwords(text)
	    # remove additional words
	    text = self.remove_padwords(text)
	    return text

	#fuzzy match???
	def compute_fuzz_score(self,word1,word2):
		return fuzz.token_sort_ratio(word1, word2)