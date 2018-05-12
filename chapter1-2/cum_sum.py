import sys
def cumutative(list):
 c=[]
 length=len(list)
 c=[sum(list[0:x + 1]) for x in range(0, length)]
 print c


n=int(input('enter the limit'))
a=[0 for i in range(n)]
for i in range(n):
 a[i]=int(input('enter the nmbrs:'))
cumutative(a)

