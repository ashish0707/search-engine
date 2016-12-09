
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
from evaluation import Effectiveness

myGenerator = NGramGenerator()
myGenerator.generate_cleaned_files("/Users/ashishbulchandani/PycharmProjects/final-project/cacm",
                                   "/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")

myGenerator.generateUnigramCorpus("/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")

# filter stop words from unigram corpus
for line in open('/Users/ashishbulchandani/PycharmProjects/final-project/common_words.txt'):
    myGenerator.one_gram_corpus.pop(line.rstrip('\n'), None)


queryProcessor = QueryProcessor()
querie_dict = queryProcessor.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm.query')

bm25 = BM25(myGenerator.one_gram_corpus,
            '/Users/ashishbulchandani/PycharmProjects/final-project/cacm.rel.txt',
            '/Users/ashishbulchandani/PycharmProjects/final-project/run_task3/task3_bm25_with_stopping_run.txt')

eval = Effectiveness()
eval.setFilePaths("/Users/ashishbulchandani/PycharmProjects/final-project/run_task3/evalutation_bm25_with_stopping/Map.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/run_task3/evalutation_bm25_with_stopping/Mrr.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/run_task3/evalutation_bm25_with_stopping/p_at_k.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/run_task3/evalutation_bm25_with_stopping/table_precision_recal.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/cacm.rel.txt")

begin = datetime.datetime.now()
for query_number,query in querie_dict.items(): #run for all quries
    bm25.rank_and_StoreDocument(query_number,query)
    eval.start_prog(bm25.sorted_rank_list, query_number)

print eval.printResults()
print "Query Processed in ==> " + str(datetime.datetime.now() - begin)
