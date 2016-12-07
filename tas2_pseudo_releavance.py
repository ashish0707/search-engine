""" steps :

get top 100 documents using TF-IDF weights
generate Doc by term freqency from main dictonary for top 100 documents
take top 5 words
"""
from collections import defaultdict

import collections

from Generator import NGramGenerator
from tf_idf_similarity import TfIdfSimilarity
from QueryListGenerator import QueryProcessor



myGenerator = NGramGenerator()
myGenerator.generateUnigramCorpus()
tfidf = TfIdfSimilarity(myGenerator.one_gram_corpus, myGenerator.total_docs)
queryProcessor = QueryProcessor()
querie_dict = queryProcessor.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm.query')

# Input, parse the query and generate weight for each term
query_word_and_tf = defaultdict(int)
query_number = 1
updated_querie_dict=dict()

for query_number, query in querie_dict:

    word_dict=defaultdict()
    doc_term_matrix = tfidf.createDoc_TermFrequency_Matix()

    query_word_and_tf = defaultdict(int)
    for word in query.split():
        query_word_and_tf[word] += 1

    docid_by_score_dict = tfidf.calculateSimilarity(query_word_and_tf)
    sortedDocIds = sorted(docid_by_score_dict.items(), key=lambda t: t[1], reverse=True)

    counter = 1
    for docKey, score in collections.OrderedDict(sortedDocIds).items():
        if counter > 10 :
            break
        dict_words = doc_term_matrix[docKey].word_and_weight_dict
        for k,v in dict_words.items():
            if k in word_dict:
                word_dict[k] +=v
            else:
                word_dict[k]=v

    word_dict_sorted = sorted(word_dict.items(), key=lambda t: t[1], reverse=True)

    updated_query=" "
    counter=1
    for k in word_dict_sorted.keys():


        if counter >10:
            break
        # if not in sort list
        updated_query += k + " "
        counter +=1

    updated_querie_dict[query_number]= query + updated_query

for query_number, query in querie_dict:
    doc_by_tf_dict = tfidf.rank_and_store_documents(query, query_number)







