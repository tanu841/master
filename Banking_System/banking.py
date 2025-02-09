from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0



class SavingsAccount:
    def __init__(self):
        self.savings_account={}

    def createAccount(self,name,initial_deposit):
        self.account_number=randint(10000,99999)
        self.savings_account[self.account_number]=[name,initial_deposit]
        print("Account Creation Successful, Account Number:",self.account_number)
    def authenticate(self,name,account_number):
        if account_number in self.savings_account.keys():
            if self.savings_account[account_number][0]==name:
                print("Authentication Successful")
                self.account_number=account_number
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False


    def withdraw(self,withdrawal_amount):
        if withdrawal_amount>self.savings_account[self.account_number][1]:
            print("Insufficient Balance")
        else:
            self.savings_account[self.account_number][1]-=withdrawal_amount
            print("Withdrawal Successful")
            self.display_balance()

    def deposit(self,deposit_amount):
        self.savings_account[self.account_number][1]+=deposit_amount
        print("Deposit Successful")
        self.display_balance()

    def display_balance(self):
        print("Avaialble Balance:", self.savings_account[self.account_number][1])


savings_account=SavingsAccount()
while True:
    print("Enter 1 to create new account")
    print("Enter 2 to access existing account")
    print("Enter 3 to exit")
    user_choice=int(input())
    if user_choice == 1:
        print("Enter Your Name:")
        name=input()
        print("Enter Initial Deposit:")
        deposit=int(input())
        savings_account.createAccount(name,deposit)
    if user_choice == 2:
        print("Enter Your Name:")
        name=input()
        print("Enter Your Account Number:")
        account_number=int(input())
        authenticationStatus=savings_account.authenticate(name,account_number)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to Withdraw")
                print("Enter 2 to Deposit")
                print("Enter 3 to Display Balance")
                print("Enter 4 to go back to previous menu")
                user_choice=int(input())
                if user_choice is 1:
                    print("Enter Withdrawal Amount")
                    withdrawal_amount=int(input())
                    savings_account.withdraw(withdrawal_amount)
                if user_choice is 2:
                    print("Enter Deposit Amount")
                    deposit_amount=int(input())
                    savings_account.deposit(deposit_amount)
                if user_choice is 3:
                    savings_account.display_balance()
                if user_choice is 4:
                    break

    if user_choice is 3:
        quit()