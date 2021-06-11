from datetime import datetime

class Account:
    def __init__(self,name,phone):
     self.name=name
     self.phone=phone
     self.balance=0
     self.loan=0
     self.loan_limit=500
     self.transactions=[]

    def deposit(self,amount):
        try:
                1+amount
        except TypeError:
            return f"The amount must be in figures"
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
        try:
                1+amount
        except TypeError:
            return f"The amount must be in figures"

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
            self.loan=0
            return f"Thank you,You have cleared your loan {self.loan} and the new balance is {self.balance}"
    
    
    def transfer(self,amount,account):
        try:
                1+amount
        except TypeError:
            return f"The amount must be in figures"

        if amount<0:
             return f"Your {amount} is less then zero"

        fee = amount*0.05
        if amount+fee>self.balance:
            return f"Your account balance is {self.balance}, you need {amount+fee}" 
        else:
         self.balance-=amount+fee
         account.deposit(amount)
         return f"You have transfered successfully"  


class MMAccount(Account):
    def __init__(self, name, phone,serviceProvider):
        super().__init__(name,phone)
        self.serviceProvider=serviceProvider
        self.limit = 500  
    def buy_airtime(self,amount):

        
        try:
                1+amount
        except TypeError:
            return f"The amount must be in figures"

        if amount<5:
            return f"Dear {self.name} you have purchase 5 and above airtime"
        else:
        
            self.balance-=amount
            return f"Dear {self.name} you have successfully purchased {amount} your new banace is {self.balance}"
        
                       

             
       



