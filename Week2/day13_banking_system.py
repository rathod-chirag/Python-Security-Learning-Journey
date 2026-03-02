"""
Day 13: Banking system
Date: March 2, 2026
Description: Full working banking system.
"""
import random
from datetime import datetime


class BankAccount:
    total_accounts = 0

    def __init__(self, owner_name, initial_balance=0):
        self.__account_number = random.randint(1000000000, 9999999999)
        self.__owner_name = owner_name
        self.__balance = initial_balance
        self.__transaction_history = []

        BankAccount.total_accounts += 1

        if initial_balance > 0:
            self.__add_transaction("Initial Deposit", initial_balance)

    # ---------------- PROPERTIES ----------------
    @property
    def owner(self):
        return self.__owner_name

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    # ---------------- PRIVATE METHOD ----------------
    def __add_transaction(self, t_type, amount):
        transaction = {
            "type": t_type,
            "amount": amount,
            "balance": self.__balance,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.__transaction_history.append(transaction)

    # ---------------- PUBLIC METHODS ----------------
    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return False

        self.__balance += amount
        self.__add_transaction("Deposit", amount)

        print(f"✅ Deposited ₹{amount:.2f}")
        print(f"   New Balance: ₹{self.__balance:.2f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False

        if amount > self.__balance:
            print("❌ Insufficient funds!")
            print(f"   Available Balance: ₹{self.__balance:.2f}")
            return False

        self.__balance -= amount
        self.__add_transaction("Withdrawal", amount)

        print(f"✅ Withdrawn ₹{amount:.2f}")
        print(f"   Remaining Balance: ₹{self.__balance:.2f}")
        return True

    def get_transaction_history(self):
        return self.__transaction_history.copy()

    def display_info(self):
        print("\n" + "=" * 50)
        print(f"Account Type : {self.__class__.__name__}")
        print(f"Owner Name  : {self.__owner_name}")
        print(f"Account No  : {self.__account_number}")
        print(f"Balance     : ₹{self.__balance:.2f}")
        print("=" * 50)

    # ---------------- MAGIC METHODS ----------------
    def __str__(self):
        return f"{self.owner}'s Account | Balance: ₹{self.balance:.2f}"

    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.balance})"


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    print("=" * 50)
    print("       🏦 BANKING SYSTEM TEST")
    print("=" * 50)

    account = BankAccount("John Doe", 1000)
    account.display_info()

    account.deposit(500)
    account.withdraw(300)
    account.withdraw(1500)

    print("\nAccount Object:")
    print(account)

    print("\n📜 Transaction History:")
    for t in account.get_transaction_history():
        print(f"- {t['type']} | ₹{t['amount']:.2f} | Balance: ₹{t['balance']:.2f} | {t['timestamp']}")

    print(f"\n🏦 Total Bank Accounts Created: {BankAccount.total_accounts}")