import sys
def fact(x):
 if x==0:
  return 1
 else:
  return x * fact(x-1) 




a=int(input('enter the nmbr : '))
print fact(a)
