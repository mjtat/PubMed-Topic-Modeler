#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:29:41 2017

@author: michelle
"""
import sys
from gensim import corpora, models

class TopicModel(object):
    '''
    The class topic_model() primarily uses the gensim package to do transformations on
    a corpus of text, in order to do some sort of analysis on it (e.g., word2vec,
    latent semantic indexing/analysis, latent dirchelet allocation, simple analyses
    like unigram and bigram frequencies). Use of this class assumes you've already
    pulled relevant PubMed articles pubmed_query() and cleaned_text() classes.

    In particular, topic_model currently runs a latent semantic indexing algorithm
    to retrieve potentially relevant topics from each abstract. There is no upper
    limit to topics to retrieve.

    topic_model takes two arguments: the dictionary that has been cleansed, and the
    number of topics you want to retrieve. Currently, it will output two variables,
    the topics themselves, and the semantic scores for each document.

    Currently, the goal is to later append title names and PMID numbers to each
    documents semantic score in order for the end user to retrieve a particular
    article from PubMed manually if they wish.

    The class can be invoked using the following syntax:

        x,y = TopicModel(dictionary_of_tokenized_text, topics).model_lsi()

    '''

    def __init__(self, text_dict, num_topics):
        self.text_dict = text_dict
        self.num_topics = num_topics

    def check_tokens(self):
        '''
        Checks if tokens are formatted appropriately.
        '''

        if not self.text_dict[self.text_dict.keys[0]][0] or self.text_dict[self.text_dict.keys[0]][1] or self.text_dict[self.text_dict.keys[0]][2] or self.text_dict[self.text_dict.keys[0]][3]:
            sys.exit('Invalid dictionary size / format.')
        elif type(self.num_topics) != int:
            sys.exit('Invalid number of topics.')

    def create_dictionary(self):
        '''
        The helper function create_dictionary() creates a gensim corpus from the
        input token dictionary, and returns the dictionary object and a corpus of
        text.
        '''

        corpus_dict = []
        for key in self.text_dict:
            corpus_dict.append(self.text_dict[key][3])
            dictionary = corpora.Dictionary(corpus_dict)
        return dictionary, corpus_dict

    def create_vectors(self):

        '''
        The helper function create_vectors() takes a dictionary and corpus object,
        then applies term-frequency inverse document frequency (TF-IDF) vectorization
        on the corpus. It again returns the dictionary, and the vectorized corpus.
        '''

        dictionary, texts = self.create_dictionary()
        corpus = [dictionary.doc2bow(text) for text in texts]
        tfidf = models.TfidfModel(corpus)
        corpus_tfidf = tfidf[corpus]
        return dictionary, corpus_tfidf

    def model_lsi(self):

        '''
        The model_lsi() function takkes the vectorized corpus, and applies
        latent semantic indexing / analysis, and returns the potential topics
        gleaned from the text, and semantic scores for each document. Each
        document is assigned a score for each topic. The highest score may
        indicate which topic the document is represented by.

        model_lsi() returns the topics, and a dictionary of PMIDs with n
        number of topic scores.
        '''

        dictionary, corpus_tfidf = self.create_vectors()
        lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=self.num_topics)
        corpus_lsi = lsi[corpus_tfidf]
        score_dict = {}
        for i in xrange(len(self.text_dict.keys())):
            for j in xrange(self.num_topics):
                score_dict.setdefault(self.text_dict.keys()[i], []).append(corpus_lsi[i][j][1])

        for i in xrange(len(lsi.print_topics())):
            j = i + 1
            print '''
        
            ###########
            # TOPIC %i #
            ###########
            
            '''  % j
            print str(lsi.print_topics()[i][1][2:-1])
        print '\n%i topics successfully extracted.\n' % self.num_topics
        print '''
        #########################
        # PMIDs by Topic Scores #
        #########################
        '''

        for key, value in score_dict.iteritems():
            print key, value
        return lsi, score_dict
    