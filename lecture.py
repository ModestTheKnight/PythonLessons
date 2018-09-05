def forit (mystate=[]):
    if len(mystate)<3:
        mystate.append(" ")
        return " "

import itertools, math

it1=iter([1,2,3,4,5])
it2=iter(forit,None)
print [x for x in it1]
print [x for x in it2]
print [x for x in enumerate('abcd')]
print sorted('sjfhbauweyfbi')

lst3=map(lambda x: math.sin(0.4*x), range(30))
for k, i in itertools.groupby(lst3, lambda x: x>0):
    #print k, i
    print k, list(i)
