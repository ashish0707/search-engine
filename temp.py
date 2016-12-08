
import math
import re

hello =dict()

hello['vabhai'] = 1
hello['chai'] = 1
hello['chu'] = 1
hello['global'] = 1
hello['randi'] = 1

if 'global' in hello:
    print "global present"


def getFormatedDockey(docKey):
    space = " "
    for i in range(70 - len(docKey)):
     space += " "
    docKey += space
    return docKey

match = re.match(r'# \d+', "# 123")
if match:
    print "match found"
else:
    print "match not found"
#
# stop_word_list = [line.rstrip('\n') for line in open('/Users/ashishbulchandani/PycharmProjects/final-project/common_words')]
# for word in stop_word_list:
#     print word

# Interface Score :
#  method calculateScore()
#
# Class A implements Score:
#  method calculateScore():
#         return 1
#
# Class B implements Score:
#  method calculateScore():
#         return 2
#
# Score = new A()
# Score.calculateScore()
#
# Score = new B()
# Score.calculateScore()