
from collections import defaultdict

import collections
import os
import math

class BM25:

    matrix_of_doc_by_term = dict()
    sorted_rank_list = []

    def __init__(self, unigramIndex,path_to_relavent_doc,fileName_bm25_run):
        self.k1 = 1.2
        self.k2 = 100
        self.b = 0.75
        self.fileName_bm25_run = fileName_bm25_run
        self.relevant = defaultdict(list)
        self.unigramIndex = unigramIndex
        self.posting_list = dict()
        self.rankBM25Dict = dict()
        self.doc_file_lenght = dict()
        self.path_to_relavent_doc = path_to_relavent_doc

        pass




    def calculate_avgDL(self,cleaned_file_path = '/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files'):
        counter_total = 0
        # path where 1000 files containing tokens for each wiki article is placed
        for file in os.listdir(cleaned_file_path):
            completeName = os.path.join(cleaned_file_path, file)
            listofwords = open(completeName).read().split()
            counter_total += len(listofwords)
            self.doc_file_lenght[file[:-4]] = len(listofwords)
        return counter_total


    def rank_and_StoreDocument(self, query_number, query):

        sorted_rank_list = self.calculateSimilarity(query_number, query)
        rank = 1
        with open(self.fileName_bm25_run, 'a') as _file_:
            for docKey, score in collections.OrderedDict(sorted_rank_list).items():
                formatedText = "%d  Q0  " % query_number
                formatedText += " " + docKey + "  %d   %f BM25_similarity" % (rank, score)
                _file_.write(formatedText + "\n")
                rank += 1
                if rank > 100:
                    break

            _file_.close()


    def calculateSimilarity(self,query_number, query):


        avdl=self.calculate_avgDL()/3204
        relevant_docs=self.relevant_doc(self.path_to_relavent_doc)

        R = len(relevant_docs[query_number])

        query_word_and_tf = defaultdict(int)
        for word in query.split():
            query_word_and_tf[word] += 1

        for term in query.split():
            if term in self.unigramIndex:
                r = 0
                posting_list=self.unigramIndex[term].docTermFreqDict

                for v in relevant_docs[query_number]:
                    if v in posting_list:
                        r+=1
                # qf=query.get[term,0]
                qf = query_word_and_tf[term]

                n = len(posting_list)
                for doc, v in posting_list.items():
                    tf = v
                    dl = self.doc_file_lenght[doc]
                    if doc in self.rankBM25Dict:
                        self.rankBM25Dict[doc] += self.score_BM25(n, tf, qf, r, R, 3204, dl, avdl)
                    else:
                        self.rankBM25Dict[doc] = self.score_BM25(n, tf, qf, r, R, 3204, dl, avdl)

        self.sorted_rank_list = sorted(self.rankBM25Dict.items(), key=lambda t: t[1], reverse=True)
        return self.sorted_rank_list

    def score_BM25(self, n, tf, qf, r,R, N, dl, avdl):
        K = self.compute_K(dl, avdl)
        first = math.log(((r + 0.5) / (R - r + 0.5)) / ((n - r + 0.5) / (N - n - R + r + 0.5)))
        second = ((self.k1 + 1) * tf) / (K + tf)
        third = ((self.k2+1) * qf) / (self.k2 + qf)
        return first * second * third

    def compute_K(self, dl, avdl):
        return self.k1 * ((1-self.b) + self.b * (float(dl)/float(avdl)))

    def relevant_doc(self,path_to_relavent_doc='/Users/ashishbulchandani/PycharmProjects/final-project/cacm.rel.txt'):
        n = 0
        my_file = open(path_to_relavent_doc, "r")
        lines = my_file.readlines()
        for line in lines:
            query=line.split()
            self.relevant[query[0]].append(query[2])
        return self.relevant

    def createDoc_TermFrequency_Matix(self):
        for word, v in self.unigramIndex.items():
            for docId, tf in v.docTermFreqDict.items():
                if docId not in self.matrix_of_doc_by_term:
                    self.matrix_of_doc_by_term[docId] = Weights()
                self.matrix_of_doc_by_term[docId].add_word_and_weight(word, tf, 1)  # in this case weight is just tf
        return self.matrix_of_doc_by_term

class Weights:

    def __init__(self):
        self.doc_length = 0
        self.word_and_weight_dict = dict()
        pass

    def add_word_and_weight(self, word, tf, idf):
        weight = tf*idf
        self.word_and_weight_dict[word] = weight
        # t = word + " ==> %f" %weight
        # print t
        self.doc_length += (weight ** 2)


