import re

from bs4 import BeautifulSoup
import os.path


class QueryProcessor:

    def __init__(self):
        pass

    def get_query_list(self, filename):
        querydict = dict()
        my_file = open(filename, "r")
        lines = my_file.read()
        soup = BeautifulSoup(lines, "html.parser")
        p_tags = soup.find_all('doc')
        for node in p_tags:
            a = (''.join(node.findAll(text=True))).split("\n", 1)
            b = a[1].strip().split(" ", 1)
            query=b[1].replace("\n", " ")
            querydict[int(b[0])] = self.generate_clean_query(query)

        return querydict

    def generate_clean_query(self, query):
        cleaned_query = re.sub(r'[^\,\.\-\w\s]', '', query)
        new_cleaned_query = ""
        for word in cleaned_query.split():
            new_cleaned_query += self.clean_word(word) + " "
        # print new_cleaned_query
        return new_cleaned_query

    def clean_word(self, word):
        if re.match(r'\d+.*,*\d+', word):
            word = word.rstrip(",")
            word = word.rstrip(".")
            return word.lower()
        else:
            return re.sub(r'[^\-\w\s]', '', word).lower()




# q = QueryProcessor()
# qdict = q.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm.query')
#
# for k,v in qdict.items():
#     print k
#     print v
#     print "\n"
