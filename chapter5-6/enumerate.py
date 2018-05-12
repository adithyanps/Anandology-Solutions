import sys
import itertools
def enum(x):
 return itertools.izip(range(len(list(x))),list(x))
d=enum(['a','b','c'])
for i,j in d:
  print i,j
