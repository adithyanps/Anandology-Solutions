import sys
def invert(x):
 d={}
 list=x.items()
 i=0
 while i<len(list):
  d[list[i][1]]=list[i][0]
  i=i+1
 return d


print invert({'x':1,'y':2,'z':3})
