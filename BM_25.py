
from collections import defaultdict

import collections
import os
import datetime
from math import log

import math

from Generator import NGramGenerator


# #without stopping
from QueryListGenerator import QueryProcessor

myGenerator = NGramGenerator()
myGenerator.generateUnigramCorpus()
# index=myGenerator.one_gram_corpus

queryProcessor = QueryProcessor()
querie_dict = queryProcessor.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm.query')
folder = '/Users/ashishbulchandani/PycharmProjects/final-project/run_task1'
fileName_bm25_run = folder + "/task1_bm25_run.txt"
posting_list=dict()
rankBM25Dict=dict()
doc_file_lenght = dict()


def calculate_avgDL():
    counter_total = 0
    # path where 1000 files containing tokens for each wiki article is placed
    save_path = '/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files'

    for file in os.listdir(save_path):
        completeName = os.path.join(save_path, file)
        listofwords = open(completeName).read().split()
        counter_total += len(listofwords)
        doc_file_lenght[file] = len(listofwords)
    return counter_total

def rank_bm25():
    query_word_and_tf = defaultdict(int)
    avdl=calculate_avgDL()/3204
    relevant_docs=relevant_doc()
    for query_number,query in querie_dict.items(): #run for all quries

        R = len(relevant_docs[query_number])

        for word in query.split():
            query_word_and_tf[word] += 1

        for term in query.split():
            if term in myGenerator.one_gram_corpus:
                r = 0
                posting_list=myGenerator.one_gram_corpus[term].docTermFreqDict

                for v in relevant_docs[query_number]:
                    if v in posting_list:
                        r+=1
                # qf=query.get[term,0]
                qf = query_word_and_tf[term]

                n = len(posting_list)
                for doc, v in posting_list.items():
                    tf = v
                    dl = doc_file_lenght[doc]
                    if doc in rankBM25Dict:
                        rankBM25Dict[doc] += score_BM25(n, tf, qf, r, R, 3204, dl, avdl)
                    else:
                        rankBM25Dict[doc] = score_BM25(n, tf, qf, r, R, 3204, dl, avdl)

        rank = 1
        sorted_rank_dict = sorted(rankBM25Dict.items(), key=lambda t: t[1], reverse=True)

        with open(fileName_bm25_run, 'a') as _file_:
            for docKey, score in collections.OrderedDict(sorted_rank_dict).items():
                formatedText = "%d  Q0  " % query_number
                formatedText += " " + docKey + "  %d   %f BM25_similarity" % (rank, score)
                _file_.write(formatedText + "\n")
                rank += 1
                if rank > 100:
                    break

            _file_.close()

        query_number += 1




# k1 , k2 are constants,
# qf is the wqf, the within query frequency,
# tf is the wdf, the within document frequency,
# n is the number of documents in the collection indexed by this term,
# N is the total number of documents in the collection,
# r is the number of relevant documents indexed by this term,
# R is the total number of relevant documents,
# avdl is the normalised document length (i.e. the length of this document divided by the average length of documents in the collection).



k1 = 1.2
k2 = 100
b = 0.75



def score_BM25(n, tf, qf, r,R, N, dl, avdl):
    K = compute_K(dl, avdl)

    first = math.log(((r + 0.5) / (R - r + 0.5)) / ((n - r + 0.5) / (N - n - R + r + 0.5)))
    second = ((k1 + 1) * tf) / (K + tf)
    third = ((k2+1) * qf) / (k2 + qf)
    return first * second * third


def compute_K(dl, avdl):
    return k1 * ((1-b) + b * (float(dl)/float(avdl)) )


relevant=defaultdict(list)



dumm_dict_scores=dict()



def relevant_doc():

        n = 0

        file = '/Users/ashishbulchandani/PycharmProjects/final-project/cacm.rel.txt'
        my_file = open(file, "r")

        lines = my_file.readlines()

        for line in lines:

            query=line.split()

            relevant[query[0]].append(query[2])

        return relevant

rank_bm25()