
class Account:
    bank_name= "saving account"
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
        
    def withdraw(self, amount):
        if amount >= self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
    
    def display_balance(self):
        print(f"Current balance is {self.balance}.")


# create instances of each class





account1 = Account("John", 1000, "12345")
account2 = Account("Jane", 2000, "67890")


# call the methods of each instance



account1.deposit(500)
account2.withdraw(1000)
