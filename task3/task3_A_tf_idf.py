from collections import defaultdict

import collections

import datetime

from Generator import NGramGenerator
from cosine_similarity import CosineSimilarity
from evaluation import Effectiveness
from tf_idf_similarity import TfIdfSimilarity
from QueryListGenerator import QueryProcessor


myGenerator = NGramGenerator()
myGenerator.generate_cleaned_files("/Users/ashishbulchandani/PycharmProjects/final-project/cacm",
                                   "/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")
myGenerator.generateUnigramCorpus("/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")

# filter stop words from unigram corpus
for line in open('/Users/ashishbulchandani/PycharmProjects/final-project/common_words.txt'):
    myGenerator.one_gram_corpus.pop(line.rstrip('\n'), None)


comparer = TfIdfSimilarity(myGenerator.one_gram_corpus, myGenerator.total_docs,"/task3A_tf_idf_with_stopping_run.txt")
comparer.setRunFolder("/Users/ashishbulchandani/PycharmProjects/final-project/run_task3")



queryProcessor = QueryProcessor()
querie_dict = queryProcessor.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm.query')



# Input, parse the query and generate weight for each term
query_word_and_tf = defaultdict(int)

eval = Effectiveness()
eval.setFilePaths("/Users/ashishbulchandani/PycharmProjects/final-project/run_task3/evalution_tf_idf_stopping/Map.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/run_task3/evalution_tf_idf_stopping/Mrr.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/run_task3/evalution_tf_idf_stopping/p_at_k.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/run_task3/evalution_tf_idf_stopping/table_precision_recal.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/cacm.rel.txt")

begin = datetime.datetime.now()
for query_number, query in querie_dict.items():
    comparer.rank_and_store_documents(query, query_number)
    eval.start_prog(comparer.sortedDocIds, query_number)

print eval.printResults()
print "Query Processed in ==> " + str(datetime.datetime.now() - begin)

