from collections import defaultdict, OrderedDict
import os

class Effectiveness:


    relevant=defaultdict(list)
    avg_precision = dict()
    rr= dict()
    p_5 = OrderedDict()
    p_20 = OrderedDict()
    dumm_dict_scores=dict()
    map_file_path = ''
    mrr_file_path = ''
    p_at_k_file_path = ''
    precision_recal_table_file_path = ''
    relevant_file_path = ""

    def setFilePaths(self,map_file_path,mrr_file_path,p_at_k_file_path,precision_recal_table_file_path,relevant_file_path):
        self.precision_recal_table_file_path= precision_recal_table_file_path
        self.map_file_path = map_file_path
        self.mrr_file_path = mrr_file_path
        self.p_at_k_file_path = p_at_k_file_path
        self.relevant_file_path = relevant_file_path


    def printResults(self):

        print "Mean_Avg_Precision = "
        print sum(self.avg_precision.values())/64

        with open(self.map_file_path, 'w') as _file_:
            formatedText = "Mean_Avg_Precision = " + str(sum(self.avg_precision.values())/64)
            _file_.write( formatedText + "\n")
            _file_.close()

        with open(self.mrr_file_path, 'w') as _file_:
            formatedText = "MRR = " + str(sum(self.rr.values()) / 64)
            _file_.write(formatedText + "\n")
            _file_.close()

        with open(self.p_at_k_file_path, 'w') as _file_:
            formatedText = "Precision At Rank 5 "
            _file_.write(formatedText + "\n")
            for query_number , v in self.p_5.items():
                formatedText = query_number + "     " + str(v)
                _file_.write(formatedText + "\n")

            formatedText = "Precision At Rank 20 "
            _file_.write(formatedText + "\n")
            for query_number , v in self.p_20.items():
                formatedText = query_number + "     " + str(v)
                _file_.write(formatedText + "\n")

            _file_.close()


    def relevant_doc(self):
            my_file = open(self.relevant_file_path, "r") # path of relavent file
            lines = my_file.readlines()
            for line in lines:
                query=line.split()
                self.relevant[query[0]].append(query[2])
                # print query[0] + " " + query[2]
            return self.relevant

    def start_prog(self,list_of_score, query_number):
        relevant_dict = self.relevant_doc()
        counter = 0
        query_n = query_number

        flag_rr = False
        query_no = str(query_n)
        count_rel = 0.0
        p = OrderedDict()
        r = OrderedDict()
        precision = 0.0
        if query_no in relevant_dict:
            for doc_id in list_of_score:
                counter += 1
                doc_id = doc_id[0]
                if doc_id in relevant_dict[query_no]:
                    count_rel += 1
                    precision += count_rel / counter
                    if flag_rr is False:
                        self.rr[query_no] = 1.0 / counter

                        # print mrr
                        flag_rr = True

                if counter is 5:
                    self.p_5[query_no] = count_rel / counter
                elif counter is 20:
                    self.p_20[query_no] = count_rel / counter

                p[doc_id] = count_rel / counter

                r[doc_id] = count_rel / len(relevant_dict[query_no])

                if counter >= 100:
                    break
                if count_rel == 0:
                    self.avg_precision[query_no] = 0.0
                else:
                    self.avg_precision[query_no] = precision / count_rel


        with open(self.precision_recal_table_file_path, 'a') as _file_:
            formatedText = self.getFormatedValue("Query_No")
            formatedText += " " + self.getFormatedValue("Doc_id")
            formatedText += " " + self.getFormatedValue("Precision")
            formatedText += " " + self.getFormatedValue("Recal")
            _file_.write(formatedText + "\n")
            for doc_id, v in p.items():
                formatedText = self.getFormatedValue(query_no) + " " + self.getFormatedValue(doc_id) + " " + self.getFormatedValue(v) + " " + self.getFormatedValue(r[doc_id])
                _file_.write(formatedText + "\n")
            _file_.close()

    def getFormatedValue(self, value):
        value = str(value)
        space = " "
        for i in range(15 - len(value)):
            space += " "
        value += space
        return value