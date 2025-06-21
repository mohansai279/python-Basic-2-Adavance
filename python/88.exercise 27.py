 #Python Program to solve a problem using Class and Objects(OOP concepts)
#Then, create an object for the account holder 
# "Ramesh" with a balance of 1000, 
# deposit 200, withdraw 500, and try to 
# withdraw 1000. Display the account details before and after transactions.
class BankAccount:
    def __init__(self, name, balance):
        self.account_holder = name
        self.balance = balance
        
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Deposited {amount}  to your account")
        
    def withdraw(Self,amount):
        if amount>Self.balance:
            print(" not enought balance")
            
        else:
            Self.balance-=amount
            
        
    def __str__(self):
        return f"Account Holder name: {self.account_holder} \nBalance: {self.balance}"

obj = BankAccount("Ramesh", 1000)
print(obj)
obj.deposit(200)
obj.withdraw(500)
print(obj)
obj.withdraw(1000)