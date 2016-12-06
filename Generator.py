import os
import re
from collections import defaultdict

import datetime

from DocumentParser import Parser


class NGramGenerator:

    def __init__(self):
        self.total_docs = 0

    one_gram_corpus = dict()
    myParser = Parser()
    docId = 1
    def generateUnigramCorpus(self, folder="cacm"):

        relpath = "/Users/ashishbulchandani/PycharmProjects/final-project/cacm/" #path for raw files
        cleaned_file_path = "/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files/"  #path to store cleaned files

        print "Generating corpus... will take around 25 secs. please be patient."

        begin = datetime.datetime.now()
        for filename in os.listdir(folder):
            raw_body_text = self.myParser.parse_document(relpath + filename)
            cleaned_body_text = re.sub(r'[^\,\.\-\w\s]', '', raw_body_text)  #apply regex on text extracted from html

            cfilename = re.sub(r'[^\w\d]', '', filename)[:-4] + ".txt"
            with open(cleaned_file_path + cfilename, 'a') as _file_:

                for word in cleaned_body_text.split():
                        cleaned_word = self.clean_word(word)                 # cleans the word using regex
                        self.add_to_one_gram_corpus(cleaned_word, filename)  # adds unique words to the unigram corpus
                        _file_.write(cleaned_word.encode('utf8') + " ")      # write the cleaned word to the file

            _file_.close()

            self.saveMapping(self.docId, filename)
            self.docId += 1

        print "Time to generate Unigram Corpus => " + str(datetime.datetime.now() - begin)
        print "Lenght of one gram corpus is : -> %d" % len(self.one_gram_corpus)
        print  self.docId
        self.total_docs = self.docId - 1  #last document number minus 1 will be the total number of files in being indexed

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

    def clean_word(self, word):
        if re.match(r'\d+.*,*\d+', word):
            word = word.rstrip(",")
            word = word.rstrip(".")
            return word.lower()
        else:
            return re.sub(r'[^\-\w\s]', '', word).lower()


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