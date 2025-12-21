class BankAccount:
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited: {amount}\nNew Balance: {self.balance}")
        else:
            print("Deposit must be positive")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance!")
        elif amount<=0:
            print("Withdraw amount must be positive")
        else:
            self.balance-=amount
            print(f"Withdraw: {amount}\nRemaining Balance: {self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.holder}\nCurrent Balance: {self.balance}")

        