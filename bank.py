
class Account:

 def __init__(self,name,phone):   
    self.name=name
    self.phone=phone
    self.balance=0

 def activity(self,amount):
      self.balance+=amount
      return f"Dear {self.name} you have deposited {self.amount} your new balance is {self.balance}"

def show__balance(self):
    return self.balance

def deposit(self,amount):
    if amount <= 0:
        return f"the amount is greater then zero"
    else:
         self.balance += amount
         return f"Hello {self.name} your is lowre then {self.amount} {self.balance} "

def withdrew(self,amount,balance):
     if amount > 0:
         return f"Your {self.amount} must be greater than zero"
     elif amount < balance:
         return f"Your {self.amount} must be less than {self.balance}"
     else:
         return f"{self.amount} reduces the {self.balance}"

# 
#     if 

