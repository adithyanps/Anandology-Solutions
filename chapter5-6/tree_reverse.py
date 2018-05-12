import sys
def reverse(x):
 i = 0 
 while i<len(x):
  if isinstance(x[i],list):
   reverse(x[i])
  i=i+1
 x.reverse()
 return x

print reverse([[1,2],[3,[4,5]],6])
