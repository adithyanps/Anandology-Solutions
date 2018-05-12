import sys
def dic(a,result=None):
 if result is None:
  result = {}
 for x in a:
  y=a[x]
  if isinstance(y,dict):
   new={}
   for z in y:
    new[str(x)+'.'+str(z)]=y[z]
   dic(new,result)
  else:
   result[x]=y
 return result

print dic({'a':1,'b':{'x':2,'y':3},'c':4})
