#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:41:31 2017

@author: michelle
"""
import nltk
from nltk.corpus import stopwords


'''
The class cleaned_text() does all the basic preprocessing necessary before vectorizing
strings (using term frequency inverse document frequency). This entails tokenizing
all the text, removing low information stop words (e.g., words like 'the', 'and', 'as'
etc.) and lemmatizing all the words to make them as uniform as possible.

The cleaned_text() class takes a dictionary object returned from the PubMed query tool.

To return a dictionary with the cleansed text, you can use the following syntax:
    
    cleaned_text(dict_here).clean()
    
Cleaned text will appear in the fourth element (index 3) in for each item in the
dictionary, and can be queried using the following syntax:
    
    dictionary[key][3]

'''
class cleaned_text:
    
    def __init__(self, text_dict):
        self.text_dict = text_dict

    '''
    The check_dict() helper function kills the process if the dictionary is in the inappropriate format.
    '''

  #  def check_dict(self):
  #      if not self.text_dict[self.text_dict.keys[0]][0] or self.text_dict[self.text_dict.keys[0]][1] or self.text_dict[self.text_dict.keys[0]][2]:
   #         sys.exit('Invalid dictionary size / format.')
         
    def clean(self):
   #     self.check_dict()
        stop_words = stopwords.words('english')
        etc_stop = ['.', ',', '?', '!', '\'',  ':', '\"', '{', '}', ';', '%', '[', ']', '(', ')', 'attributes=', 'methods', 'label', 'u\'methods', 'u\'label', 'u\'nlmcategory', 'u\'conclusions', 'u\'conclusions', 'u\'discussion', 'u\'results', 'u\'objectives', 'stringelement', 'u\'method', 'u\'objective']
        stop_words = stop_words + etc_stop
        
        for key, value in self.text_dict.iteritems():
            value = str(value[2])
            value = value.lower()
            value = nltk.word_tokenize(value)
            stopped_tokens = [i for i in value if not i in stop_words]
            lemmatized_tokens = [nltk.WordNetLemmatizer().lemmatize(i) for i in stopped_tokens]
            self.text_dict[key].append(lemmatized_tokens)
            
        print '\n Successfully cleaned and tokenized abstracts.'
        return self.text_dict
        


