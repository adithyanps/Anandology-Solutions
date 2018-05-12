import sys
import os
def count(x):
 list=os.listdir(x)
 i=0
 d={}
 while i < len(list):
  list[i]=list[i].split('.')
  if(len(list[i])>1):
   d[list[i][1]]=d.get(list[i][1],0)+1
  i=i+1
 return d
 #for j,k in d.items():
 # print j,k
print count(sys.argv[1])
