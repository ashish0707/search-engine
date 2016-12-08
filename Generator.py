import os
import re
import shutil
from collections import defaultdict

import datetime

from DocumentParser import Parser


class NGramGenerator:

    def __init__(self):
        self.total_docs = 0

    one_gram_corpus = dict()
    myParser = Parser()
    docId = 1

    def generateUnigramCorpus(self, folder="cacm/", cleaned_file_path="cleaned_files/"):

        self.generate_cleaned_files(folder, cleaned_file_path)
        begin = datetime.datetime.now()
        for filename in os.listdir(cleaned_file_path):

            # if self.docId > 1:
            #     break

            abs_fileName = os.path.join(cleaned_file_path, filename)
            for word in open(abs_fileName).read().split():
                self.add_to_one_gram_corpus(word, filename[:-4])  # adds unique words to the unigram corpus


            self.docId += 1

        print "Time to generate Unigram Corpus => " + str(datetime.datetime.now() - begin)
        print "Lenght of one gram corpus is : -> %d" % len(self.one_gram_corpus)
        self.total_docs = self.docId - 1
        print "Total Documents :=> %d" % self.total_docs

    def generate_cleaned_files(self, folder="cacm/", cleaned_file_path="cleaned_files/"):

         if not os.path.exists(folder):
            print "Generating cleaned files... will take around 15 secs. please be patient."
            os.mkdir(cleaned_file_path[:-1])
            for filename in os.listdir(folder):
                raw_body_text = self.myParser.parse_document(folder+filename)
                for line in raw_body_text.split("\n"):
                    if not re.match(r'\d+', line.strip("\n").strip(" ")):
                        cleaned_body_text = re.sub(r'[^\,\.\-\w\s]', '', line)  # apply regex on text extracted from html
                        cfilename = re.sub(r'[^\w\d]', '', filename)[:-4] + ".txt"
                        with open(cleaned_file_path + cfilename, 'a') as _file_:

                            for word in cleaned_body_text.split():
                                cleaned_word = self.clean_word(word)  # cleans the word using regex
                                _file_.write(cleaned_word.encode('utf8') + " ")  # write the cleaned word to the file

                        _file_.close()
         else:
             print "cleaned files exist"


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


# ng = NGramGenerator()
# ng.generateUnigramCorpus("/Users/ashishbulchandani/PycharmProjects/final-project/cacm",
#                          "/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_files")
# ng.generate_cleaned_files("/Users/ashishbulchandani/PycharmProjects/final-project/")