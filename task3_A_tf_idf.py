from collections import defaultdict

import collections

import datetime

from Generator import NGramGenerator
from cosine_similarity import CosineSimilarity
from tf_idf_similarity import TfIdfSimilarity
from QueryListGenerator import QueryProcessor


myGenerator = NGramGenerator()
myGenerator.generateUnigramCorpus("/Users/ashishbulchandani/PycharmProjects/final-project/cacm",
                                  "/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")

# filter stop words from unigram corpus
for line in open('/Users/ashishbulchandani/PycharmProjects/final-project/common_words.txt'):
    myGenerator.one_gram_corpus.pop(line.rstrip('\n'), None)


comparer = TfIdfSimilarity(myGenerator.one_gram_corpus, myGenerator.total_docs,"/task3A_tf_idf_with_stopping_run.txt")
comparer.setRunFolder("/Users/ashishbulchandani/PycharmProjects/final-project/run_task3")



queryProcessor = QueryProcessor()
querie_dict = queryProcessor.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm.query')



# Input, parse the query and generate weight for each term
query_word_and_tf = defaultdict(int)
query_number = 1


counter = 1
begin = datetime.datetime.now()
for query_number, query in querie_dict.items():
    comparer.rank_and_store_documents(query, query_number)
print "Query Processed in ==> " + str(datetime.datetime.now() - begin)
