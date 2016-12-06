import os
from collections import defaultdict

import datetime


class NGramGenerator:

    def __init__(self):
        pass

    one_gram_corpus = dict()

    def generateUnigramCorpus(self, folder="cleaned_files"):

        relpath = "/Users/ashishbulchandani/PycharmProjects/HW4/cleaned_files/"
        print "Generating corpus... will take around 15 secs. please be patient."
        docId = 1
        begin = datetime.datetime.now()
        for filename in os.listdir(folder):
            f = open(relpath+filename)
            for sentence in f:
                for word in sentence.split():
                    self.add_to_one_gram_corpus(word,filename)
            self.saveMapping(docId,filename)
            docId += 1



        print "Time to generate Unigram Corpus => " + str(datetime.datetime.now() - begin)


    # GIVEN   : a cleaned word and a documentId which is an integer
    # RETURNS : adds the word to one gram corpus.
    def add_to_one_gram_corpus(self, word, documenId):
        if word not in self.one_gram_corpus:
            self.one_gram_corpus[word] = Posting()
        self.one_gram_corpus[word].addToDocTermFreqDict(documenId)
        # print len(self.one_gram_corpus)

    def saveMapping(self, doc_id, filename):
        with open("mapping.txt", 'a') as _file_:
            tempData = "%d ==> " % doc_id + filename + "\n"
            _file_.write(tempData)
        _file_.close()

    def get_uni_gram_corpus(self):
        return self.one_gram_corpus


class Posting:
    def __init__(self):
        self.total = 0
        self.docTermFreqDict = defaultdict(int)
        pass

    def addToDocTermFreqDict(self,documentId):
        self.docTermFreqDict[documentId] += 1
        self.total += 1

    def __cmp__(self, posting):
        if self.total < posting.total:
            return -1
        if self.total == posting.total:
            return 0
        if self.total > posting.total:
            return 1

#
# ng = NGramGenerator()
# ng.generateUnigramCorpus()