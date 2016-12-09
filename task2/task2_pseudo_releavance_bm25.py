""" steps :

get top 100 documents using TF-IDF weights
generate Doc by term freqency from main dictonary for top 100 documents
take top 5 words
"""
from collections import defaultdict

import collections

import datetime

from BM_25 import BM25
from Generator import NGramGenerator
from evaluation import Effectiveness
from tf_idf_similarity import TfIdfSimilarity
from QueryListGenerator import QueryProcessor



myGenerator = NGramGenerator()
myGenerator.generate_cleaned_files("/Users/ashishbulchandani/PycharmProjects/final-project/cacm",
                                           "/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")

myGenerator.generateUnigramCorpus("/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")


bm25 = BM25(myGenerator.one_gram_corpus,
            '/Users/ashishbulchandani/PycharmProjects/final-project/cacm.rel.txt',
            '/Users/ashishbulchandani/PycharmProjects/final-project/run_task2/task2_psuedo_rel_bm25_run.txt')


queryProcessor = QueryProcessor()
querie_dict = queryProcessor.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm.query')

# Input, parse the query and generate weight for each term
updated_querie_dict=dict()

begin = datetime.datetime.now()

dict_of_stop_word = dict()
for line in open('/Users/ashishbulchandani/PycharmProjects/final-project/common_words.txt'):
    dict_of_stop_word[line.replace("\n", "")] = 1

for query_number, query in querie_dict.items():

    word_dict=defaultdict()
    doc_term_matrix = bm25.createDoc_TermFrequency_Matix()

    sortedDocId_list = bm25.calculateSimilarity(query_number,query)

    counter = 1
    for docKey, score in collections.OrderedDict(sortedDocId_list).items():
        # print docKey
        if counter > 3:
            break
        dict_words = doc_term_matrix[docKey].word_and_weight_dict
        for k,v in dict_words.items():
            if k in word_dict:
                word_dict[k] += v
            else:
                word_dict[k]=v
        counter+=1

    word_dict_sorted = sorted(word_dict.items(), key=lambda t: t[1], reverse=True)


    updated_query=""
    counter=1
    for k in collections.OrderedDict(word_dict_sorted).keys():

        if k not in dict_of_stop_word:
            if counter > 10:
                # print updated_query
                break
            # if not in sort list


            updated_query += k + " "
            counter += 1

    updated_querie_dict[query_number]= query + updated_query
    print updated_querie_dict[query_number]

eval = Effectiveness()
eval.setFilePaths("/Users/ashishbulchandani/PycharmProjects/final-project/run_task2/evalutation_query_exp_bm25/Map.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/run_task2/evalutation_query_exp_bm25/Mrr.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/run_task2/evalutation_query_exp_bm25/p_at_k.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/run_task2/evalutation_query_exp_bm25/table_precision_recal.txt",
                  "/Users/ashishbulchandani/PycharmProjects/final-project/cacm.rel.txt")


for query_number,query in querie_dict.items(): #run for all quries
    bm25.rank_and_StoreDocument(query_number,query)
    eval.start_prog(bm25.sorted_rank_list, query_number)

print eval.printResults()
print "Query Processed in ==> " + str(datetime.datetime.now() - begin)







