#!/usr/bin/env python
# coding: utf-8

"""
Owwaksyon Smart Topic Tagger
Accesses a Google Sheet populated by Chatbot and tags each response with a topic and priority 
"""

__author__ = "JC Peralta"
__version__ = "0.1.0"
__license__ = "CC-BY"


import sys
sys.path.append("..")


import numpy as np
import pandas as pd

from re import sub

from utils.tag_topic import TopicPriorityTag
from utils.clean_comments import CommentCleaner

import gspread as gs
import os
import time


def main():
    
    gc = gs.service_account(filename='../creds/service_account.json')
    sheets_url= 'https://docs.google.com/spreadsheets/d/1chiatozuGjEau08fr_c1qAHzysPa0ubRoJknqoZaEIs'
    N_ATTEMPTS = 3
    print('\n')
    print('==========================================================')
    print('OWWAksyon Smart Topic Tagger Run: %s' % pd.Timestamp.now().strftime("%Y-%m-%d %I:%M:%S %p"))
    start_time = time.time()
    print('Accessing chatbot responses sheet... ' , end='')
    for i in np.arange(N_ATTEMPTS):
        try:
            sh = gc.open_by_url(sheets_url)
            ws = sh.worksheet('Responses')
            table_df = pd.DataFrame(ws.get_all_records())
            if ws:
                print('DONE!')
                break
            time.sleep(2)
        except:
            print("Retrying.." , end='')

    print('Checking new responses... ', end='')
    # Get and update only new entries -  those which have
    table_df = table_df[table_df['Priority']=='']
    # if no new entries, exit
    if len(table_df)==0:
        print('nothing to update! Exiting...')
        print('\n')
    else:
        print('Tagging %d new responses... ' % len(table_df), end = '')
        cleaner = CommentCleaner()
        tagger = TopicPriorityTag()
        table_df['Short Text'] = table_df['Concern'].apply(lambda x: cleaner.clean_comment(x))
        table_df['Category'] = table_df['Short Text'].apply(lambda x: tagger.tag_topic_category(x))
        table_df['Priority'] = table_df['Category'].apply(lambda x: tagger.tag_topic_priority(x))
        table_df['Category'] = table_df['Category'].apply(lambda x: '; '.join(x))

        for i in table_df.index:
            # Short Text : G
            ws.update("I%d" % (i+2), table_df['Short Text'].loc[i])
            #Category : H
            ws.update("J%d" % (i+2), table_df['Category'].loc[i])
            #Priority : I
            ws.update("K%d" % (i+2), str(table_df['Priority'].loc[i]))
            time.sleep(2)

        print( 'DONE!')
        end_time = time.time()
        print( 'All updates done in %0.1f secs.' % (end_time-start_time))
        print('\n')
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()




