#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This part of the project focuses on identifying fake jobs using the following dataset from kaggle: https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction.
#This code is also inspired by the idea of Shivam Burnwal (2020)

#import

import numpy as np
import pandas as pd

import os
for dirname, _, filenames in os.walk('/kaggle/input/real-or-fake-fake-jobposting-prediction/fake_job_postings.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[2]:


#still import and install

get_ipython().system('pip install missingno')
get_ipython().system('pip install plotly.express')
get_ipython().system('pip install wordcloud')
get_ipython().system('pip install spacy')
get_ipython().system('pip install xgboost')
get_ipython().system('pip install -U spacy[lookups]')
get_ipython().system('pip install imblearn')
#!pip install RandomUnderSampler
get_ipython().system('pip install spacy')
get_ipython().system('pip install wordcloud')
get_ipython().system('pip install sklearn')
get_ipython().system('pip install -U scikit-learn')

import re
import string
import random
import missingno
import en_core_web_sm
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

import spacy
from wordcloud import WordCloud
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from spacy.lang.en.examples import sentences

import imblearn
from imblearn.under_sampling import RandomUnderSampler

import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin
from sklearn.metrics import accuracy_score, recall_score, plot_confusion_matrix
from sklearn.svm import SVC

import warnings
warnings.filterwarnings("ignore")


# In[3]:


data = pd.read_csv('C:\\mun_fake_job_postings.csv')
print(data)


# In[4]:


data.head()


# In[5]:


data.describe()

#Interpreting the data, the columns "telecommuting", "has_company_logo" and "has_questions" may be removed.
#We can also see that only ~0.05% of the dataset consists of fraudulent/fake jobs, which calls for a need for oversampling/undersampling. In this code, oversampling was used.


# In[6]:


#Removing of irrelevant columns and replacing null values

columns=['job_id', 'telecommuting', 'has_company_logo', 'has_questions', 'salary_range', 'employment_type']
for col in columns:
    del data[col]

data.fillna(' ', inplace=True)


# In[7]:


#Spliting of data

def split(location):
    l = location.split(',')
    return l[0]

data['country'] = data.location.apply(split)


# In[8]:


country = dict(data.country.value_counts()[:11])
del country[' ']
plt.figure(figsize=(8,6))
plt.title('No. of job postings country wise', size=20)
plt.bar(country.keys(), country.values())
plt.ylabel('No. of jobs', size=10)
plt.xlabel('Countries', size=10)

#We can see in this graph that the dataset mostly represents the US.
#Thus, given this dataset, predictions may be inaccurate when applied in the Philippines.
#However, this can be easily remedied by training this model with a dataset focused on jobs in the Philippines, once that dataset is available.


# In[9]:


#Merging of data

data['text']=data['title']+' '+data['location']+' '+data['company_profile']+' '+data['description']+' '+data['requirements']+' '+data['benefits']
del data['title']
del data['location']
del data['department']
del data['company_profile']
del data['description']
del data['requirements']
del data['benefits']
del data['required_experience']
del data['required_education']
del data['industry']
del data['function']
del data['country']

data.head()


# In[10]:


#Wordcloud visualization

fraudjobs_text = data[data.fraudulent==1].text
actualjobs_text = data[data.fraudulent==0].text


# In[11]:


#Wordcloud - Fraudulent Jobs

STOPWORDS = spacy.lang.en.stop_words.STOP_WORDS
plt.figure(figsize = (16,14))
wc = WordCloud(min_font_size = 3,  max_words = 3000 , width = 1600 , height = 800 , stopwords = STOPWORDS).generate(str(" ".join(fraudjobs_text)))
plt.imshow(wc,interpolation = 'bilinear')


# In[12]:


#Wordcloud - Real Jobs

plt.figure(figsize = (16,14))
wc = WordCloud(min_font_size = 3,  max_words = 3000 , width = 1600 , height = 800 , stopwords = STOPWORDS).generate(str(" ".join(actualjobs_text)))
plt.imshow(wc,interpolation = 'bilinear')


# In[13]:


#Cleaning Data

# Create our list of punctuation marks
punctuations = string.punctuation

# Create our list of stopwords
nlp = en_core_web_sm.load()
stop_words = spacy.lang.en.stop_words.STOP_WORDS

# Load English tokenizer, tagger, parser, NER and word vectors
parser = English()

# Creating our tokenizer function
def spacy_tokenizer(sentence):
    # Creating our token object, which is used to create documents with linguistic annotations.
    mytokens = parser(sentence)

    # Lemmatizing each token and converting each token into lowercase
    mytokens = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]

    # Removing stop words
    mytokens = [word for word in mytokens if word not in stop_words and word not in punctuations ]

    # return preprocessed list of tokens
    return mytokens


# In[14]:


# Custom transformer using spacy

class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        # Cleaning text
        return [clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}

# Function to clean text
def clean_text(text):
    return text.strip().lower()


# In[15]:


#Generation of matrix of occurence of words

#bow_vector = CountVectorizer(min_df=0, max_df=1, binary=False, tokenizer = spacy_tokenizer, ngram_range=(1,3))
bow_vector = CountVectorizer(token_pattern=r"(?u)\b\w+\b", stop_words=None, ngram_range=(2,2), analyzer='word')
#bow_vector.build_analyzer()
#bow_vector.fit_transform(smallcorp.split('\n'))


# In[16]:


#Splitting of dataset into training and test sets + Oversampling

X_train, X_test, y_train, y_test = train_test_split(data.text, data.fraudulent, test_size=0.3)

'''
under = RandomUnderSampler(sampling_strategy=1)
print("Before oversampling: ",Counter(y_train))
X_train, y_train = under.fit_resample(X_train, y_train)
print("After oversampling: ",Counter(y_train))
X_test, y_test = under.fit_resample(X_test, y_test)

under = RandomUnderSampler(sampling_strategy=1)
X, y = under.fit_resample(X, y)
'''


# In[17]:


#Logistic Regression Model

#bow_vector_train_reviews = bow_vector.fit_transform(X_train)
#bow_vector_test_reviews = bow_vector.transform(X_test)

clf = LogisticRegression()

# Create pipeline
pipe = Pipeline([('cleaner', predictors()),
                 ('vectorizer', bow_vector),
                 ('classifier', clf)])

# Fitting our model
pipe.fit(X_train, y_train)


# In[18]:


# Predicting with a test dataset
predicted = pipe.predict(X_test)

# Model accuracy
print("Logistic Regression Accuracy:", accuracy_score(y_test, predicted))
print("Logistic Regression Recall:", recall_score(y_test, predicted))


# In[20]:


plot_confusion_matrix(pipe, X_test, y_test, cmap='Blues', values_format=' ')


# In[ ]:





# In[ ]:





# In[ ]:




