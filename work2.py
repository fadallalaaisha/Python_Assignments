from datetime import datetime

class Account:
    def __init__(self,name,phone,transactions):
     self.name=name
     self.phone=phone
     self.balance=0
     self.loan=0
     self.loan_limit=500
     self.transactions=[]

    def deposit(self,amount):
        if amount<=0:
            return f"Your {amount} is greater then zero"
        else:
            self.balance += amount
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Depasit"}
            self.transactions.append(transaction)
        # return f"Hello {self.name} your have {self.transaction}"
         #return f"Hello {self.name} your have deposit {amount} and yiur balance is {self.balance}"
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

    def get_statement(self):
        for transaction in self.transactions:
             narration=transaction["narration"]
             amount=transaction["amount"]
             balance=transaction["balance"]
             time=transaction["time"]
             print(f"{time.strftime('%D')}..{narration}..{amount}..{balance}")

    def replay_loan(self,amount):
        if amount<0:                
            return f"You have {amount} amount of money and your balance is {self.balance}"
        elif amount<self.loan:
            self.loan-=amount
            return f"You have paid {amount} and the remaining loan is {self.loan}"
        else:
            difference=amount-self.loan
            self.balance+=difference
            return f"Thanks you have cleared your loan {self.loan} and the new balance is {self.balance}"

               



