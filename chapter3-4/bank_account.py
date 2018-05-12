import sys
class bankaccount:
 def __init__(self):
  self.balance=0
 def withdraw(self,amount):
  self.balance -= amount
  print self.balance
 def deposit(self,amount):
  self.balance+=amount
  print self.balance
a=bankaccount()
b=bankaccount()
a.deposit(100)
b.deposit(150)
b.withdraw(50)
a.withdraw(40)
