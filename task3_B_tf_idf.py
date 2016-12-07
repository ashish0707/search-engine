from collections import defaultdict

import collections

import datetime

from Generator import NGramGenerator
from cosine_similarity import CosineSimilarity
from tf_idf_similarity import TfIdfSimilarity
from QueryListGenerator import QueryProcessor


#without stopping
myGenerator = NGramGenerator()
myGenerator.generateUnigramCorpus("cacm_stem", "cleaned_stemmed_files")
comparer = TfIdfSimilarity(myGenerator.one_gram_corpus, myGenerator.total_docs,"/Users/ashishbulchandani/PycharmProjects/final-project/")
queryProcessor = QueryProcessor()
querie_dict = queryProcessor.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm_stem.query')

# Input, parse the query and generate weight for each term
query_word_and_tf = defaultdict(int)
query_number = 1


for query_number, query in querie_dict:
    comparer.rank_and_store_documents(query, query_number,"task3_b_run.txt")

