"""
Day 9 : Encapsulation.
Date: February 25, 2026
Description: Learning data protection with private attributes.

"""

# Example 1: The problem.
print("="*50)
print("Example 1: Why we need encapsulation.")
print("="*50)

class BadAccount:

    def __init__(self,balance):
        self.balance = balance

bad = BadAccount(1000)
print(f"Starting balance: $ {bad.balance}")

# Anyone can do  this:
bad.balance = -5000 # Negative balance!

print(f"Balance tampering: ${bad.balance}")
print("This is BAD!\n")

# Example 2: The solution.
print("="*50)
print("Example 2: USING PRIVATE ATTRIBUTES.")
print("="*50)

class GoodAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance # this is a private variable

    def get_balance(self):
        return self.__balance
    
    def deposite(self,amount):
        if amount > 0:
            self.__balance += amount

        print(f"Deposited: ${amount}")

    def withdraw(self,amount):
        if amount < 0:
            print("Amount must be positive!")
        elif amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdraw : ${amount}")
    

good = GoodAccount("Alice",1000)

# Cant access balance directly.
try:
    print(good.__balance)
except AttributeError:
    print("Cant access __balance directly.")

# must use method 
print(f"Balance: ${good.get_balance()}")

# Methods validation
good.deposite(-200)
good.deposite(500)
good.withdraw(2000)
good.withdraw(500)

print(f"Final balance: ${good.get_balance()}\n")

# Example 3: Property Decorator.
print("="*50)
print("Example 3: Property Decorator.")
print("="*50)

class ModernAccount:

    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    """Getter - read the balance"""
    @property
    def balance(self):
        return self.__balance
    
    """Setter set balance with validation."""
    @balance.setter
    def balance(self,amount):
        if amount < 0:
            print("Amount must be positive!")
        else:
            self.__balance += amount
            print(f"balance updated to ${amount}")
        
modern = ModernAccount("Steve",1000)

print(f"Balance: ${modern.balance}")

modern.balance = 2000
modern.balance = -500

print(f"Final balance: ${modern.balance}\n")