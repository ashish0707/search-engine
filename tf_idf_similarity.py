import os
from collections import defaultdict
from math import log

import math

import collections

import datetime

import shutil

from SimilarityMeasure import SimilarityMeasure


class TfIdfSimilarity(SimilarityMeasure):

        sortedDocIds = []
        matrix_of_doc_by_term = dict()

        def __init__(self, corpus, no_of_docs,filename_for_run):
            self.filename_for_run = filename_for_run
            self.corpus = corpus
            self.no_of_docs = no_of_docs
            self.createDoc_TermWeight_Matix()
            self.relPath = ""
            pass

        def setRunFolder(self, folderPath):
            self.relPath = folderPath
            self.filename_for_run = self.relPath + self.filename_for_run
            if os.path.isdir(self.relPath):
                if os.path.isfile(self.filename_for_run):
                    os.remove(self.filename_for_run)
            else:
                os.mkdir(self.relPath)

        def set_matrix_of_doc_by_term(self,matrix_of_doc_by_term):
            self.matrix_of_doc_by_term = matrix_of_doc_by_term

        # creates a document by word and term weight matrix where weight is tf*idf
        def createDoc_TermWeight_Matix(self):
            for word, v in self.corpus.items():
                idf = log(self.no_of_docs/len(v.docTermFreqDict)) + 1  # this calculates idf for word
                for docId, tf in v.docTermFreqDict.items():
                    if docId not in self.matrix_of_doc_by_term:
                        self.matrix_of_doc_by_term[docId] = Weights()
                    self.matrix_of_doc_by_term[docId].add_word_and_weight(word, tf, idf)

        def createDoc_TermFrequency_Matix(self):
            for word, v in self.corpus.items():
                for docId, tf in v.docTermFreqDict.items():
                    if docId not in self.matrix_of_doc_by_term:
                        self.matrix_of_doc_by_term[docId] = Weights()
                    self.matrix_of_doc_by_term[docId].add_word_and_weight(word, tf, 1) #in this case weight is just tf
            return self.matrix_of_doc_by_term

        def calculateSimilarity(self,query_word_and_weigth):
            doc_score = dict()
            for docid, v in self.matrix_of_doc_by_term.items():
                score = 0
                for word, weight in query_word_and_weigth.items():
                    word_with_slash_n = word
                    if word_with_slash_n in v.word_and_weight_dict:
                        score += v.word_and_weight_dict[word_with_slash_n] * weight

                # doc_score[docid] = score/math.sqrt(v.doc_length * length_of_query)
                doc_score[docid] = score  # score is not normalized. Length of the document will affect the score.
            return doc_score


        def rank_and_store_documents(self, query, query_number=0):

            query_word_and_tf = defaultdict(int)
            for word in query.split():
                query_word_and_tf[word] += 1

            # get each document score for the given query
            doc_and_score_dict = self.calculateSimilarity(query_word_and_tf)

            # sort the documents in descending order of their score
            self.sortedDocIds = sorted(doc_and_score_dict.items(), key=lambda t: t[1], reverse=True)

            # save the top 100 files as best match for given query
            rank = 1

            with open(self.filename_for_run, 'a') as _file_:
                for docKey, score in collections.OrderedDict(self.sortedDocIds).items():
                    formatedText = "%d  Q0  " % query_number

                    formatedText += self.getFormatedDockey(docKey) + "  %d   %f tf_idf_similarity" % (
                    rank, score)
                    _file_.write(formatedText + "\n")
                    rank += 1
                    if rank > 100:
                        break
                        # print (formatedText)

            _file_.close()
            query_number += 1


        def getFormatedDockey(self, docKey):
            space = " "
            for i in range(60 - len(docKey)):
                space += " "
            docKey += space
            return docKey


# this class holds weights for each word and sum of each weight is the weight of the document.
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


