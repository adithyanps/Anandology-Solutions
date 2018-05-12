import sys 
def dups(x):
 print set([i for i in x if x.count(i) > 1])

a=[1,2,2,2,3,4,2,1,5,6,4,9]
dups(a)
