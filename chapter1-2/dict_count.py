import sys
def count(x):
 a=open(x).read().split()
 d={}
 for i in a:
  d[i]=d.get(i,0)+1
 c=d.items()
 c.sort(key=lambda x:x[1])
 for (i,j) in c:
  print i
count(sys.argv[1])

