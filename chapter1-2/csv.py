import sys
def csv(x):
 f=open(x).read().split()
 i=0
 while i < len(f):
  f[i]=f[i].split(',')
  i=i+1 
 return f


print csv(sys.argv[1])
