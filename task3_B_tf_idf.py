import os
import re
from collections import defaultdict

import collections

import datetime

from Generator import NGramGenerator
from cosine_similarity import CosineSimilarity
from tf_idf_similarity import TfIdfSimilarity
from QueryListGenerator import QueryProcessor


#generate stem documents

query_number = 1

folder = "/Users/ashishbulchandani/PycharmProjects/final-project/cacm_stem"
if not os.path.exists(folder):
    os.makedirs(folder)
    fileHandle = open(str(query_number) + ".txt", 'w+')
    for line in open("/Users/ashishbulchandani/PycharmProjects/final-project/cacm_stem.txt", 'r'):

        if re.match(r'# \d+', line.rstrip("\n")):

            #close previous file
            if not query_number == 1:
                fileHandle.write("\n<pre>\n<html>")
                fileHandle.close()

            #open new file

            fileHandle = open(folder + "/" + str(query_number) + ".html", 'w+')

            fileHandle.write("<html>\n<pre>\n")
            query_number += 1

        else:
            lineWithSpaces = line
            line = line.replace("\n","").replace(" ","")
            if not line.isdigit():
                fileHandle.write(lineWithSpaces)
            else:
                print lineWithSpaces

else:
    print "directory available"


myGenerator = NGramGenerator()
myGenerator.generateUnigramCorpus("/Users/ashishbulchandani/PycharmProjects/final-project/cacm_stem",
                                  "/Users/ashishbulchandani/PycharmProjects/final-project/cleaned_stemmed_file")


comparer = TfIdfSimilarity(myGenerator.one_gram_corpus, myGenerator.total_docs,"/task3B_tf_idf_stemmed_run.txt")
comparer.setRunFolder("/Users/ashishbulchandani/PycharmProjects/final-project/run_task3")

queryProcessor = QueryProcessor()
query_number = 1
query_dict = dict()
for line in open('/Users/ashishbulchandani/PycharmProjects/final-project/cacm_stem.query', 'r'):
    query_dict[query_number] = queryProcessor.generate_clean_query(line)
    query_number += 1

# Input, parse the query and generate weight for each term
query_word_and_tf = defaultdict(int)
query_number = 1


for query_number, query in query_dict.items():
    print query
    comparer.rank_and_store_documents(query, query_number)

