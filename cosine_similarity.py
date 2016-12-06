from math import log

import math


class CosineSimilarity:

        matrix_of_doc_by_term = dict()

        def __init__(self):
            pass

        def set_matrix_of_doc_by_term(self,matrix_of_doc_by_term):
            self.matrix_of_doc_by_term = matrix_of_doc_by_term

        def createMatix(self, corpus, no_of_docs):
            for word, v in corpus.items():
                idf = log(no_of_docs/len(v.docTermFreqDict)) + 1  # this calculates idf for word
                for docId, tf in v.docTermFreqDict.items():
                    if docId not in self.matrix_of_doc_by_term:
                        self.matrix_of_doc_by_term[docId] = Weights()
                    self.matrix_of_doc_by_term[docId].add_word_and_weight(word, tf, idf)



        def calculateSimilarity(self,query_word_and_weigth,length_of_query):
            doc_score = dict()
            for docid, v in self.matrix_of_doc_by_term.items():
                score = 0
                for word, weight in query_word_and_weigth.items():
                    word_with_slash_n = word
                    if word_with_slash_n in v.word_and_weight_dict:
                        score += v.word_and_weight_dict[word_with_slash_n] * weight

                doc_score[docid] = score/math.sqrt(v.doc_length * length_of_query)
            return doc_score

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


