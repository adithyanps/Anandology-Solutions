import sys
def reverse(x):
 f=open(x).readlines()
 d = f[::-1]
 return [ x.replace('\n', ' ') for x in d]
print reverse('she.txt')
