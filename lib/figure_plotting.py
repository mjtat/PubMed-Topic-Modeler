#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:54:11 2017

@author: michelle
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class topic_barplot:
    
    def __init__(self, topics, topic_scores):
        self.topics = topics
        self.topic_scores = topic_scores
        
    def plot(self):
        
        topic_lists = {}
        
        for i in xrange(len(self.topics.show_topics())):
            j = i + 1
            topic_lists[j] = []
            
        num_topics = len(self.topics.show_topics())
        print num_topics
        
        for score in self.topic_scores.itervalues():
            for i in xrange(num_topics):
                topic_lists[i+1].append(abs(score[i]))
                
        PMID = []
        
        for key in self.topic_scores.iterkeys():
            PMID.append(key)
            
        df = pd.DataFrame.from_dict(topic_lists)
        df['PMID'] = PMID
        
        fig, ax = plt.subplots()
        df.iloc[:,0:num_topics].plot(kind = 'bar', stacked = True, figsize=(16, 10), ax=ax, width = .8, fontsize = 20)
        ax.set_title("LSI Topic Score by PubMed ID", fontsize = 24)
        ax.set_xticklabels(df['PMID'], rotation = 90)
        ax.set_xlabel("Article (PubMed ID)",fontsize = 18)
        ax.set_ylabel("Topic Score", fontsize = 18)
        ax.legend(fontsize = 20)
        fig.tight_layout()
        plt.savefig('barplot.png', dpi = 800)
