#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:06:08 2017

@author: michelle
"""
import os
os.chdir('/home/michelle/CS_Specialization')
import unittest
import pubmed_testing as pt
import preprocessing as pp
import topic_modeling as tm

'''
class pubmedtest() is a class that conducts unit testing in python. It uses the 
unittest module in python, and tests if edge cases I came up with work with
the scripts or not. Based on unit testing results, I went back and modified
my prior scripts to make different default requirements for input, otherwise the
scripts will not run.
'''

class pubmedtest(unittest.TestCase):
    
    def test_num_query(self):
        cases = [5,10,20,30,40,50,60,70,80,90,100,200]
        for number in cases:
            self.assertTrue(pt.pubmed_query('tatinthehat@gmail.com', 'anxiety', number).return_abstracts())
    
    '''
    test_keywords_1() theoretically should work. test_keywords_2() will break intentionally
    because I tell the script to stop when some weird term is entered.
    '''
    
    def test_keywords_1(self):
        keywords = ['anxiety', 'depression', 'PTSD'] 
        for word in keywords:
            self.assertTrue(pt.pubmed_query('tatinthehat@gmail.com', word, 10).return_abstracts())
    
    '''
    test_dictionary() tests if the dictionary is the right shape (and therefore, has 
    the correct data).
    '''
    
    def test_dictionary(self):
        pubmed = pt.pubmed_query('tatinthehat@gmail.com', 'anxiety', 100).return_abstracts()
        for key in pubmed.iterkeys():
            self.assertTrue(pubmed[key][0])
            self.assertTrue(pubmed[key][1])
            self.assertTrue(pubmed[key][2])
    
    '''
    test_topic_input() is the same as above, but checks if the third index of the
    dictionary exists.
    '''
    
    def test_topic_input(self):
        pubmed = pt.pubmed_query('tatinthehat@gmail.com', 'anxiety', 100).return_abstracts()
        pubmed = pp.cleaned_text(pubmed).clean()
        for key in pubmed.iterkeys():
            self.assertTrue(pubmed[key][0])
            self.assertTrue(pubmed[key][1])
            self.assertTrue(pubmed[key][2])
            self.assertTrue(pubmed[key][3])
            
    '''
    test_num_topics() checks the logical extremes one could take with the number of topics
    the user could input.
    '''        
            
    def test_num_topics(self):
        pubmed = pt.pubmed_query('tatinthehat@gmail.com', 'anxiety', 100).return_abstracts()
        pubmed = pp.cleaned_text(pubmed).clean()
        self.assertTrue(tm.topic_model(pubmed, 10).model_lsi())
        self.assertTrue(tm.topic_model(pubmed, 50).model_lsi())
        self.assertTrue(tm.topic_model(pubmed, 75).model_lsi())
        

#    def test_keywords_2(self):
#        keywords= [abc, 123, ' ']
#        for word in keywords:
#            self.assertTrue(pt.pubmed_query('tatinthehat@gmail.com', word, 10).return_abstracts())
            
    
if __name__ == '__main__':
    unittest.main()
    