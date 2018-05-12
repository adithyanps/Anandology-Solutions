import os
import urllib
import sys
def wget(x):
 r=urllib.urlopen(x)
 cont=r.read()
 name=x.split('/')
 n=name[-1]
 if n=='':
  n='index.html'
 f=open(n,'w')
 f.write(cont)
 print f



wget(sys.argv[1])
