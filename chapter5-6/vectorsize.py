import sys
def square(x):
 return x*x
def vectorsize(f):
 r=[]
 def g(x):
   for i in x:
     r.append(f(i))
   return r
 return g
f=vectorsize(square)
f([1,2,3,4])

