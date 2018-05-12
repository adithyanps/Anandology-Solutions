import sys
def enum(x):
 a=range(len(x))
 b=zip(a,x)
 return b
   


print enum(['a','b','c'])
