import sys
def cumutative(x):
 c=[]
 d=1
 for i in x:
  d=d*i
  c.append(d)
 print c



n=int(input('enter the limit'))
a=[0 for i in range(n)]
for i in range(n):
 a[i]=int(input('enter the nmbrs : '))
cumutative(a)
