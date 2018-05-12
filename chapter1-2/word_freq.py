import sys
def freq(x):
 dict = {}
 for i in x:
  dict[i] = dict.get(i,0) + 1
 return dict

a=input("enter a string")
print freq(a)
