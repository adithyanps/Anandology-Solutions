import sys
def prodct(x):
 j=1
 for i in x:
   j =j*i
 print j
n=int(input("enter the limit"))
a=[0 for i in range(n)]
for i in range(n):
 a[i]=int(input('enter the elements'))
prodct(a)
