
import math
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

print getFormatedDockey("ashish")+"."

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