"""To use this class, you can use the following syntax:

pubmed_query(email, terms, author, number_of_articles).return_abstracts()"""

import sys
from Bio import Entrez

class PubMedQuery(object):

    '''
    This class makes use of a open source PubMed API to extract pertinent information
    PubMed. At the moment, the goal for this script is to query pubmed, and extract
    abstracts for a given research domain. Later on, topic modeling will be implemented
    ,in particular, either latent semantic analysis or latent dirchelet allocation, on
    PubMed abstracts. Specifically, I am focusing on depression as an extension of my
    main Insight Project which focused on mental health.

    The pubmed_query() class extracts abstracts from PubMed. There are four
    main arguments the user can input. The required arg is email. The user
    can define terms they want to search for, the number of articles to pull, and
    if they choose, the another database other than PubMed
    '''

    def __init__(self, email, terms, num_articles, year=None, author=None, database='pubmed'):
        self.email = email
        self.database = database
        self.terms = terms
        self.num_articles = num_articles
        self.author = author
        self.year = year

    def search_check(self):
        '''
        search_check() searches evaluates some user input, and tries to catch any errors
        in the input. If it does, it prompts the user to fix their crap.
        '''
        if type(self.terms) != str or type(self.email) != str or type(self.database) != str:
            sys.exit('Invalid arguments for query.')

        elif self.email.strip() == '' or self.terms.strip() == '':
            sys.exit('You need to provide a valid email and/or search term.')

    def search_terms(self):

        '''
        search_terms() is a helper function that denotes any keywords and
        authors you want to specifically search for. If the other is none,
        the helper function just returns the initial keyword inputs.
        '''

        if self.author is None and self.year is None:
            keywords = self.terms
            query = keywords

        elif self.author is None:
            keywords = self.terms
            year = '(("%s"[Date - Publication] : "%s"[Date - Publication]))' % (self.year, self.year)
            query = keywords + ' ' + 'AND' + ' ' + year

        elif self.year is None:
            keywords = self.terms
            author = '%s[Author]' % self.author
            query = keywords + ' ' + 'AND' + ' ' + author

        else:
            keywords = self.terms
            author = '%s[Author]' % self.author
            year = '(("%s"[Date - Publication] : "%s"[Date - Publication]))' % (self.year, self.year)
            query = keywords + ' ' + 'AND' + ' ' + author + ' ' + 'AND' + ' ' + year

        return query

    def search_query(self):

        '''
        search_query() initiates the query to get potentially useful PubMed
        information, such as unique IDs, topic names, and MeSH keywords. These
        data are returned in a xml/json type nested format. Additionally, a
        dictionary of unique article IDs are returned, which will be later
        be used to retrieve article abstracts.
        '''

        Entrez.email = self.email
        query = self.search_terms()
        handle = Entrez.esearch(db='pubmed',
                                sort='relevance',
                                retmax=self.num_articles,
                                retmode='xml',
                                term=query)
        results = Entrez.read(handle)
        id_dictionary = {}
        for i in xrange(len(results['IdList'])):
            j = i + 1
            id_dictionary['Article #%i' % j] = results['IdList'][i]
        return results, id_dictionary

    def return_abstracts(self):
        '''
        return_abstracts() is the main function that will return a dictionary of
        PubMed IDs (PMIDs), article titles, and article names. To accommplish this,
        the function digs into the mutliply nested dictionary the PubMed API returns,
        and retrieves the relevant data mentioned above.

        The second chunk of return_abstracts() loops through the retrieved query.
        It creates a dictionary consisting of the article PubMed ID (PMID),
        the article title, article publication year, and the abstract.
        '''

        self.search_check()
        results, id_dict = self.search_query()
        abstract_dict = {}
        Entrez.email = self.email
        ids = ','.join(id_dict.values())
        handle = Entrez.efetch(db=self.database,
                               retmode='xml',
                               id=ids)
        results = Entrez.read(handle)


        for i in xrange(len(results['PubmedArticle'])):
            pubmedid = int(results['PubmedArticle'][i]['MedlineCitation']['PMID'])
            title = results['PubmedArticle'][i]['MedlineCitation']['Article']['ArticleTitle']
            year = str(results['PubmedArticle'][0]['MedlineCitation']['DateCompleted'])
            year = int(year[-6:-2])
            abstract = str(results['PubmedArticle'][i]['MedlineCitation']['Article']['Abstract']['AbstractText'])
            abstract_dict[pubmedid] = [title, year, abstract]

        print '\n Successfully retrieved %i abstracts.' % self.num_articles

        return abstract_dict
