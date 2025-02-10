from abc import ABCMeta, abstractmethod
from random import randint

class BankAbstract(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self):
        return 0
    @abstractmethod
    def authenticate(self):
        return 0
    @abstractmethod
    def withdraw(self):
        return 0
    @abstractmethod
    def deposit(self):
        return 0


class savingAccount:
    def __init__(self):
        self.savingAccount={}

    def createAccount(self,name,initial_deposit):
        self.accountNo=randint(10000,99999)
        self.savingAccount[self.accountNo]=[name,initial_deposit]
        print("Account Creation Successful, Account Number:",self.accountNo)

    def authenticate(self,accountNo,name):
        if accountNo in self.savingAccount.keys():
            if self.savingAccount[accountNo][0]==name:
                print("Authentication Successful")
        else:
            print("Authentication Failed")


    def withdraw(self,accountNo,withdrawal_amount):
        if self.savingAccount[accountNo][1]<withdrawal_amount:
            print("Insufficient Balance")
        else:
            self.savingAccount[accountNo][1]=self.savingAccount[accountNo][1]-withdrawal_amount
            print("Withdrawal Successful")
            self.display_balance(accountNo)

    def deposit(self,accountNo,deposit_amount):
        self.savingAccount[accountNo][1]=self.savingAccount[accountNo][1]+deposit_amount
        print("Deposit Successful")
        self.display_balance(accountNo)

    def display_balance(self,accountNo):
        print("Available Balance:",self.savingAccount[accountNo][1])


savingAccount=savingAccount()
while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    choice=int(input())
    if choice==1:
        print("Enter your name:")
        name=input()
        print("Enter the initial deposit:")
        deposit=int(input())
        savingAccount.createAccount(name,deposit)
    elif choice==2:
        print("Enter your name:")
        name=input()
        print("Enter your account number:")
        accountNo=int(input())
        savingAccount.authenticate(accountNo,name)
        print("Enter 1 to withdraw")
        print("Enter 2 to deposit")
        print("Enter 3 to display balance")
        choice=int(input())
        if choice==1:
            print("Enter the amount to withdraw:")
            withdraw=int(input())
            savingAccount.withdraw(accountNo,withdraw)
        elif choice==2:
            print("Enter the amount to deposit:")
            deposit=int(input())
            savingAccount.deposit(accountNo,deposit)
        elif choice==3:
            savingAccount.display_balance(accountNo)
    elif choice==3:
        quit()