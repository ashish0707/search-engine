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
        # print len(p_tags)
        for node in p_tags:
            # print node
            a = (''.join(node.findAll(text=True))).split("\n", 1)
            b = a[1].strip().split(" ", 1)
            query=b[1].replace("\n", "")
            querydict[int(b[0])] = query #where b[0] is the query number

        return querydict

# q = QueryProcessor()
# qdict = q.get_query_list('/Users/ashishbulchandani/PycharmProjects/final-project/cacm.query')
#
# for k,v in qdict.items():
#     print k
#     print v
#     print "\n"
