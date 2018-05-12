import sys
import os
def lines(x):
 c=0
 for p,d,f in os.walk(os.getcwd()):
  for i in f:
   if x in i:
     print os.path.join(p,i)," :- ",len(open(i).readlines())
     c+=len(open(i).readlines())
 print c


lines(".py")








