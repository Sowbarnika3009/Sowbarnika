#Implement a class called Bank Account that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.#
class Bank_Account:
  def __init__(self):
    self.balance=0
print( " Hello !!! Welcome to the Deposit & Withdrawal Machine")
def deposit(self):
amount=float(input("Enter amount to be deposited:"))
self.balance+=amount
print("\n Amount deposited:", amount)
def withdraw(self):
  amount= float(input("Enter amount to be withdrawn:"))
  if self.balance>=amount:
    self.balance-=amount 
print("\n you withdrew:", amount)
  else:
print("\n Insufficient balance")
def display(self):
print("\n Net Available balance=",self.balance)
s=Bank_Account()
s.deposit()
s.withdraw()
s.display()