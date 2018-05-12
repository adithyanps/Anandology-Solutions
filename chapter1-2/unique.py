import sys
def unique(x):
 c=[]
 for i in x:
  if i not in c:
   c.append(i)
 print c
n=int(input('enter the limit :'))
a=[0 for i in range(n)]
for i in range(n):
 a[i]=int(input('enter the nmbrs:'))
unique(a)
