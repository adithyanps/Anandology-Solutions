import sys
from zipfile import *
def zip(x,y):
 f=Zipfile(x,'w')
 for i in y:
  f.write(i)
 print f




zip(sys.argv[1],sys.argv[2:])




