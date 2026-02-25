
"""
Day 10 : Encapsulation - Exercise.
Date: February 25, 2026
Description: Creating a secure bank account system.

"""
import random

class BankAccount:

    def __init__(self,owner_name,initial_balance,pin):
        if len(str(pin)) != 4:
            raise ValueError("PIN must be 4 digits!")

        self.__account_number =  random.randint(1000000000,9999999999)
        self.__owner_name = owner_name
        self.__balance  = initial_balance
        self.__pin = pin

        print(f"Account created for {owner_name}")
        print(f"Account: {self.__account_number}")

    def varify_pin(self,pin):
        return self.__pin == pin

    @property
    def owner(self):
        return self.__owner_name
    
    @property
    def account_number(self):
        return self.__account_number
    
    def deposit(self,amount,pin):
        if not self.varify_pin(pin):
            print("Incorrect PIN!")
            return False
        
        if amount <= 0:
            print("Amount must be positive!")
            return False
        
        self.__balance += amount

        print("Deposited ${self.__balance}")
        return True
    
    def withdraw(self,amount,pin):
        if not self.varify_pin(pin):
            print("Incorrect PIN!")
            return False
        
        if amount <= 0:
            print("Amount must be positive!")
            return False
        
        if amount > self.__balance:
            print(f"Insufficient Balance!")
            print(f"Balance: ${self.__balance}, Requested: ${amount}")
            return False
        
        self.__balance -= amount
        print(f"Withdraw: ${amount}")
        print(f"New Balance: ${self.__balance}")
        return True
    
    def check_balance(self,pin):
        if not self.varify_pin(pin):
            print("Incorrect PIN!")
            return False
        
        print(f"Current balance: ${self.__balance}")
        return self.__balance
    
    def change_pin(self,old_pin,new_pin):
        # changing pin with varification.
        if not self.varify_pin(old_pin):
            print("Incorrect PIN!")
            return False
        
        # validating new pin.
        if len(str(new_pin)) != 4:
            print("PIN must be 4 digits!")
            return False
        
        # changing the pin.
        self._pin = new_pin
        print("Pin changed successfully!")
        return True
    
if __name__ == "__main__":
    print("="*50)
    print("TESTING SECURE BANK ACCOUNT")
    print("="*50)
    
    # Test 1: Create account
    print("\n--- Test 1: Create Account ---")
    account = BankAccount("Ajay Ade ", 1000, 1234)
    
    # Test 2: Check properties
    print("\n--- Test 2: Properties ---")
    print(f"Owner: {account.owner}")
    print(f"Account #: {account.account_number}")
    
    # Test 3: Check balance
    print("\n--- Test 3: Check Balance ---")
    account.check_balance(1234)  # Correct PIN
    account.check_balance(9999)  # Wrong PIN
    
    # Test 4: Deposit
    print("\n--- Test 4: Deposit ---")
    account.deposit(500, 1234)   # Correct PIN
    account.deposit(100, 9999)   # Wrong PIN
    account.deposit(-50, 1234)   # Invalid amount
    
    # Test 5: Withdraw
    print("\n--- Test 5: Withdraw ---")
    account.withdraw(200, 1234)  # Valid
    account.withdraw(2000, 1234) # Insufficient funds
    account.withdraw(100, 9999)  # Wrong PIN
    
    # Test 6: Change PIN
    print("\n--- Test 6: Change PIN ---")
    account.change_pin(1234, 5678)  # Success
    account.check_balance(1234)     # Old PIN fails
    account.check_balance(5678)     # New PIN works
    
    # Test 7: Try to access private attributes
    print("\n--- Test 7: Try Direct Access ---")
    try:
        print(account.__balance)
    except AttributeError:
        print("❌ Can't access __balance directly!")
    
    try:
        print(account.__pin)
    except AttributeError:
        print("❌ Can't access __pin directly!")
    
    print("\n✅ All tests complete!")
    
        

        

        




        





