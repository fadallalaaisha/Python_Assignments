class Account:
 def __init__(self,name,phone,loan_limit):
     self.name=name
     self.phone=phone
     self.balance=0
     self.loan=0
     self.loan_limit=loan_limit
     #return f"My name is {self.name} and my phone number is {self.phone}"

 def deposit(self,amount):
     
     if amount<=0:
        return f"Your {amount} is greater then zero"
     else:
         self.balance += amount
         return f"Hello {self.name} your have deposit {amount} and yiur balance is {self.balance}" 

 def show__balance(self):
    return self.balance

def withdraw(self,amount):
     if amount > 0:
         return f"Dear {self.name} you have withdrawn {amount}"
     elif amount <= 0:
         return f"Your amount must be greater than zero"
     elif amount>self.balance :
         return f"You amount must be less than balance"  
     else:
         self.balance-=amount
         return f"{self.balance}"  

def borrow(self,amount):
     if amount>self.loan__limit:
      return f"The amount is greater than your limit"
     elif self.loan>0:
         return f"clear you debt amount"
     else:
         self.loan+=1
         self.balance += amount
         return f"You have successfully get loan"


