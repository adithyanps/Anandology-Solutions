import sys
import os
import time
def details(x):
 list=os.listdir(x)
 i=0
 d={}
 while i < len(list):
  p=os.stat(os.getcwd()+'/'+list[i])
  print list[i],'\t',time.ctime(p.st_mtime),'\t',p.st_size
  i=i+1
details(os.getcwd())
