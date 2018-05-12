import sys
def SUM(x):
 print sum(x)




n=int(input('enter the limit :'))
a=[0 for i in range(n)]
for i in range(n):
 a[i]=int(input('enter the nmbrs :'))
SUM(a)

