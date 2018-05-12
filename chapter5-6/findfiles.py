import sys
import os
def findfiles(x):
 for path,dirct,files in os.walk(os.getcwd()):
   if x in files:
     print os.path.join(path,x)
findfiles(sys.argv[1])
