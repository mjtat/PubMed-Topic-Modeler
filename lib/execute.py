#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:36:57 2017

@author: michelle
"""
import sys
import pubmed_query as pq
import preprocessing as pp
import topic_modeling as tm
import figure_plotting as fp

def execute(email, terms, articles, topics):
    '''
    execute() runs through the entire set of scripts to get abstracts
    and model them.
    '''
    pubmed = pq.PubMedQuery(email, terms, articles).return_abstracts()
    pubmed = pp.cleaned_text(pubmed).clean()
    topic, scores = tm.topic_model(pubmed, topics).model_lsi()
    fp.topic_barplot(topic, scores).plot()
    return topic, scores

if __name__ == '__main__':
    execute(str(sys.argv[1]), str(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
