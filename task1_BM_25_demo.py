
from collections import defaultdict

import collections
import os
import datetime
from math import log

import math

from Generator import NGramGenerator
from BM_25 import BM25

# #without stopping
from QueryListGenerator import QueryProcessor

myGenerator = NGramGenerator()
myGenerator.generate_cleaned_files("/Users/ashishbulchandani/PycharmProjects/final-project/cacm",
                                   "/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")

myGenerator.generateUnigramCorpus("/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")

queryProcessor = QueryProcessor()
querie_dict = queryProcessor.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm.query')
folder = '/Users/ashishbulchandani/PycharmProjects/final-project/run_task1'

bm25 = BM25(myGenerator.one_gram_corpus,
            '/Users/ashishbulchandani/PycharmProjects/final-project/cacm.rel.txt',
            '/Users/ashishbulchandani/PycharmProjects/final-project/run_task1/task1_bm25_run.txt')


for query_number,query in querie_dict.items(): #run for all quries
    bm25.rank_and_StoreDocument(query_number,query)

