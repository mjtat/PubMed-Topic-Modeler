#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:36:57 2017

@author: michelle
"""
import sys
sys.path.insert(0,"../scripts")
import pubmed_query as pq
import preprocessing as pp
import topic_modeling as tm
import figure_plotting as fp

class run_modeler:
    
    def __init__(self, email, terms, articles, topics):
        self.email = email
        self.terms = terms
        self.articles = articles
        self.topics = topics
        
    def execute(self):
        pubmed = pq.pubmed_query(self.email, self.terms, self.articles).return_abstracts()
        pubmed = pp.cleaned_text(pubmed).clean()
        topic, scores = tm.topic_model(pubmed, self.topics).model_lsi()
        fp.topic_barplot(topic, scores).plot()
        return topic, scores
        
if __name__ == '__main__':
        topics, scores = run_modeler('tatinthehat@gmail.com', 'anxiety', 50, 5).execute()
        # Terminal commands
        execute(str(sys.argv[1]), str(sys.argv[2:4]), int(sys.argv[5]), int(sys.argv[6])).run()