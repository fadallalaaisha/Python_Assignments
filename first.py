class Account:
 def __init__(self,name,phone):
     self.name=name
     self.phone=phone
     self.balance=0
     #return f"My name is {self.name} and my phone number is {self.phone}"

 def deposit(self,amount):
     
     if amount<=0:
        return f"Your {amount} is greater then zero"
     else:
         self.balance += amount
         return f"Hello {self.name} your have deposit {amount} and yiur balance is {self.balance}" 

 def show__balance(self):
    return self.balance

