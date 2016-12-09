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

    def generateUnigramCorpus(self, cleaned_file_path):

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

    def generate_cleaned_files(self, folder, cleaned_file_path):

         if not os.path.exists(cleaned_file_path):
            print "Generating cleaned files... will take around 15 secs. please be patient."
            os.mkdir(cleaned_file_path)
            for filename in os.listdir(folder):
                abs_fileName = os.path.join(folder, filename)
                raw_body_text = self.myParser.parse_document(abs_fileName)
                for line in raw_body_text.split("\n"):
                    previous_line = line
                    line = line.replace("\n", "").replace(" ", "").replace("\t", "")
                    if not line.isdigit():
                        cleaned_body_text = re.sub(r'[^\,\.\-\w\s]', '', previous_line)  # apply regex on text extracted from html
                        cfilename = filename[:-5] + ".txt"
                        abs_fileName = os.path.join(cleaned_file_path, cfilename)
                        with open(abs_fileName, 'a') as _file_:

                            for word in cleaned_body_text.split():
                                cleaned_word = self.clean_word(word)  # cleans the word using regex
                                _file_.write(cleaned_word.encode('utf8') + " ")  # write the cleaned word to the file

                        _file_.close()
         else:
             print "cleaned files exist"

    def generate_stopped_cleaned_files(self, folder, cleaned_file_path, stop_word_file_path):

         if not os.path.exists(cleaned_file_path):
             print "Generating cleaned files... will take around 15 secs. please be patient."

             dict_of_stop_word = dict()
             for line in open(stop_word_file_path):
                 dict_of_stop_word[line.replace("\n","")] = 1

             os.mkdir(cleaned_file_path)
             for filename in os.listdir(folder):
                 abs_fileName = os.path.join(folder, filename)
                 raw_body_text = self.myParser.parse_document(abs_fileName)
                 for line in raw_body_text.split("\n"):
                      previous_line = line
                      line = line.replace(" ", "").replace("\t", "").replace("\n","")
                      if not line.isdigit():
                         cleaned_body_text = re.sub(r'[^\,\.\-\w\s]', '', previous_line)  # apply regex on text extracted from html
                         cfilename = filename[:-5] + ".txt"
                         abs_fileName = os.path.join(cleaned_file_path, cfilename)
                         with open(abs_fileName, 'a') as _file_:
                            for word in cleaned_body_text.split():
                                cleaned_word = self.clean_word(word)  # cleans the word using regex
                                if not cleaned_word in dict_of_stop_word:
                                     _file_.write(cleaned_word.encode('utf8') + " ")  # write the cleaned word to the file

                            _file_.close()
                      else:
                          print line
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