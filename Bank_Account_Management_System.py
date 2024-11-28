'''
Bank_Account_Management_System.py

What?
This code defines a simple banking system with classes for managing bank accounts. 
It allows users to deposit, withdraw, and check their balance, as well as calculate interest for a savings account.

How?
The Bank class manages the account holder's name and balance, 
providing methods for depositing and withdrawing funds, as well as displaying the balance. 
The savingAccount class inherits from Bank and adds functionality to calculate interest based on a fixed interest rate. 
A loop at the end provides a command-line interface for user interaction.



'''

class Bank:
    def __init__(self,account_holder,balance):
        self.name=account_holder
        self.__balance=balance
    def deposit(self,balance):
        if balance>0 and balance<=10000000000:
            self.__balance+=balance
            print(f"\nDeposit {balance} and new balance = {self.__balance}\n")
        else:
            print("\nInvalid amount\n")
    def withdraw(self,balance):
        if balance>0 and balance <=self.__balance:
            self.__balance-=balance
            print(f"\nWithdraw {balance} new balance = {self.__balance}\n")
        else:
            print("\nInsufficient Balanac or Invalid amount \n")
             
    def show_balance(self):
        print(f"\nCurrent Balance {self.__balance}\n")
    def get_balance(self):
        return self.__balance
        
class SavingAccount(Bank):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)
        self.interest_rate=0.12
    def calculate_interest(self):
        print(f"\nYour interest : {self.get_balance()*self.interest_rate}\n")
        

account=SavingAccount("Abdullah Nazmus-Sakib",500.0)

while True:

    print("\n1. Check balance ")
    print("2. Deposit balance ")
    print("3. Withdraw balance ")
    print("4. Show My Interest ")
    print("5. Exit ")
    
    choice=int(input("Enter Your Choice (1-4) : "))
    
    if choice == 1:
        account.show_balance()
    elif choice == 2:
        dep_balance=float(input("\nEnter your deposit amount : "))
        account.deposit(dep_balance)
    elif choice == 3:
        wi_balance=float(input("\nEnter your withdraw amount : "))
        account.withdraw(wi_balance)
    elif choice == 4:
        account.calculate_interest()
    else:
        print("\nThank You! Have a nice day\n")
        break
