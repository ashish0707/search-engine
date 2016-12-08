from collections import defaultdict
import os

class Effectiveness:

    relevant=defaultdict(list)

    dumm_dict_scores=dict()

    def relevant_doc(self, path="/Users/ashishbulchandani/PycharmProjects/final-project/cacm.rel.txt"):
            n = 0

            my_file = open(path, "r") # path of relavent file
            lines = my_file.readlines()
            for line in lines:
                query=line.split()
                self.relevant[query[0]].append(query[2])
                print query[0] + " " + query[2]
            return self.relevant

    def start_prog(self, list_of_score):
        relevant_dict= self.relevant_doc()
        counter=0


        mean_avg_precision=0.0
        mrr=0.0
        query_n=1
        avg_precision=dict()
        p_5=dict()
        p_20=dict()
        while query_n <=64:
          query_no = str(query_n)
          if query_no in relevant_dict:
            print "inside if"
            count_rel = 0

            p = dict()
            r = dict()

            rr = 0.0
            flag_rr= False
            precision=0.0
            for doc_id in list_of_score:

                counter+=1

                if doc_id in relevant_dict[query_no]:
                    print "inside inner if"
                    count_rel+=1
                    precision+=count_rel / counter
                    if flag_rr is False:
                        rr = 1/counter
                        mrr += rr
                        flag_rr=True
                if counter is 5:
                    p_5[query_no]=count_rel / counter
                elif counter is 20:
                    p_20[query_no]=count_rel / counter


                p[doc_id] = count_rel / counter

                r[doc_id] = count_rel / len(relevant_dict[query_no])


                if counter >= 100:
                    break
            if count_rel == 0:
                avg_precision[query_no]=0
            else:
                avg_precision[query_no]=precision/count_rel
            print  "avg_precision :%d query_no" % avg_precision[query_no]
          query_n += 1
          print "processed" + str(query_n)


        total_precision_values = sum(avg_precision.values())
        print "total precision value :%d" % total_precision_values
        print "len(avg_precision) :%d" % len(avg_precision)

        mean_avg_prc = total_precision_values/len(avg_precision)

        mrr=mrr/64

        print mean_avg_prc
        print mrr




