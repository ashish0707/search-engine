from collections import defaultdict

import datetime

from Generator import NGramGenerator
from QueryListGenerator import QueryProcessor
from cosine_similarity import CosineSimilarity
from evaluation import Effectiveness

myGenerator = NGramGenerator()

myGenerator.generate_cleaned_files("/Users/ashishbulchandani/PycharmProjects/final-project/cacm",
                                   "/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")
myGenerator.generateUnigramCorpus("/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")

comparer = CosineSimilarity(myGenerator.one_gram_corpus, myGenerator.total_docs, "/task1_cosine_similarity_run.txt")
queryProcessor = QueryProcessor()
querie_dict = queryProcessor.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm.query')


# Input, parse the query and generate weight for each term
query_word_and_tf = defaultdict(int)

eval = Effectiveness()
eval.setFilePaths("/Users/ashishbulchandani/PycharmProjects/final-project/run_task1/evalution_cosine_similarity/Map.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/run_task1/evalution_cosine_similarity/Mrr.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/run_task1/evalution_cosine_similarity/p_at_k.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/run_task1/evalution_cosine_similarity/table_precision_recal.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/cacm.rel.txt")


begin = datetime.datetime.now()
for query_number, query in querie_dict.items():
    comparer.rank_and_store_documents(query,query_number)
    eval.start_prog(comparer.sortedDocIds, query_number)

print eval.printResults()
print "Query Processed in ==> " + str(datetime.datetime.now() - begin)
