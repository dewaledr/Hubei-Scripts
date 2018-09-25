'''
create a bank account class that has two attributes in Python:
•	owner
•	balance
and two methods:
•	deposit
•	withdraw
As an added requirement, withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account 
can't be overdrawn.
'''
import os


class Account:
    def __init__(self, owner, balance=0.00):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: \t\t{self.owner}\nAccounnt Balance: \t€{self.balance}'

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print(f'Deposit Accepted:\t €{dep_amt}\tBalance now is: €{self.balance} ')

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print(f'Withdrawal accepted \tBalance is €{self.balance}')
        else:
            print(f'Insufficienf funds... \tBalance is €{self.balance}')

# Clear the screen and then Instantiate the class
os.system("clear")
acct1 = Account('Francis Adepoju', 200.00)

# Print the object
print(acct1)

# Show the Account Owner attribute
acct1.owner

# Show the Account balance attribute
acct1.balance

# Make a series of deposits and withdrawals
acct1.deposit(100)
acct1.deposit(150)
acct1.deposit(1000)

acct1.withdraw(750)

acct1.withdraw(50)

acct1.withdraw(800)

