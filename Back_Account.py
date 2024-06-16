# Creating a bank account class that has two attributes 
        # Owner
        # Balance
# and has two methods
        # Deposit
        # Withdrawl
# And as an added requirement, Withdrawl may not exceed the available balance

# Example_Class:
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
        
    def deposit(self, dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
        
    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')
            
# Creating an instance of the Account class
acct1 = Account('Jose', 100)

# Printing the account details
print(acct1)

# Making a deposit
acct1.deposit(500)

# Checking the owner of the account
print(acct1.owner)  # This should print 'Jose'

acct1.withdraw(700)
        

