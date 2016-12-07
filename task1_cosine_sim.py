from collections import defaultdict

import datetime

from Generator import NGramGenerator
from QueryListGenerator import QueryProcessor
from cosine_similarity import CosineSimilarity

myGenerator = NGramGenerator()

myGenerator.generateUnigramCorpus()

comparer = CosineSimilarity(myGenerator.one_gram_corpus, myGenerator.total_docs, "/task1_cosine_similarity_run.txt")
queryProcessor = QueryProcessor()
querie_dict = queryProcessor.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm.query')


# Input, parse the query and generate weight for each term
query_word_and_tf = defaultdict(int)
query_number = 1

begin = datetime.datetime.now()
for query_number, query in querie_dict.items():
    comparer.rank_and_store_documents(query,query_number)
print "Query Processed in ==> " + str(datetime.datetime.now() - begin)
