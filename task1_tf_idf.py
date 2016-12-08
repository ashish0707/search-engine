import re
from collections import defaultdict

import collections

import datetime

from Generator import NGramGenerator
from tf_idf_similarity import TfIdfSimilarity
from QueryListGenerator import QueryProcessor
from evaluation import Effectiveness


myGenerator = NGramGenerator()
myGenerator.generate_cleaned_files("/Users/ashishbulchandani/PycharmProjects/final-project/cacm",
                                  "/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")
myGenerator.generateUnigramCorpus("/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")

comparer = TfIdfSimilarity(myGenerator.one_gram_corpus, myGenerator.total_docs,"/task1_tf_idf_similarity_run.txt")
comparer.setRunFolder("/Users/ashishbulchandani/PycharmProjects/final-project/run_task1")
queryProcessor = QueryProcessor()
querie_dict = queryProcessor.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm.query')

# Input, parse the query and generate weight for each term
query_word_and_tf = defaultdict(int)
query_number = 1


eval = Effectiveness()

counter = 1
begin = datetime.datetime.now()
for query_number, query in querie_dict.items():
    comparer.rank_and_store_documents(query, query_number)
    eval.start_prog(comparer.sortedDocIds)
    if counter > 1:
        break
print "Query Processed in ==> " + str(datetime.datetime.now() - begin)





