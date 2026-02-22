import random

"""
Day 8: Class & Objects - exercise
Date: February 22,2026
Description: Creating a class (Student,Book,BankAccount)
"""

# Exrcise 1: Student Class

print("="*50)
print("Exercise 1: STUDENT CLASS")
print("="*50)

class Student:

    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"{self.name} is {self.age} years old!")
        print(f"{self.name} score {self.grade} out of 100." )
    
    def is_passing(self):
        if self.grade >= 50:
            return True
        else:
            return False
        
    def get_latter_grade(self):
        if self.grade >= 90:
            return 'A'
        elif self.grade >= 80:
            return 'B'
        elif self.grade >= 70:
            return 'C'
        elif self.grade >= 60:
            return 'D'
        else:
            return 'F'
    
s1 = Student("Arjun",20,67)
s2 = Student("Sujal",20,89)
s3 = Student("Devanshu",20,78)

s1.display_info()
s2.display_info()
s3.display_info()

print(f"{s1.name} is passing: {s1.is_passing()}")
print(f"{s2.name} is passing: {s2.is_passing()}")
print(f"{s3.name} is passing: {s3.is_passing()}")

print(f"Student {s1.name} obtained: '{s1.get_latter_grade()}' Grade")
print(f"Student {s2.name} obtained: '{s2.get_latter_grade()}' Grade")
print(f"Student {s3.name} obtained: '{s3.get_latter_grade()}' Grade.")


# Exercise 2: Book class

print("="*50)
print("Exercise 2: BOOK CLASS")
print("="*50)

class Book:

    def __init__(self,title,author,pages,):
        self.title = title
        self.author = author
        self.pages = pages
        self.curent_page = 0

    def read(self,num_page):

        self.current_page = num_page
        
        if self.current_page > self.pages:
            self.current_page = self.pages
        
        
        print(f"Read {num_page} pages. Now on page {self.current_page}/{self.pages}")
    
    def get_progress(self):
        percentage = (self.current_page / self.pages) * 100

        return percentage
    
    def is_finished(self):
        if self.current_page == self.pages:
            print("finished!")
        else:
            print("NOt Finished!")

book = Book("Test","Author",100)
book.read(150)
print(book.get_progress())

# Exercise 3: BankAccount class

print("="*50)
print("Exercise 3: BANKACCOUNT CLASS")
print("="*50)

class BankAccount:

    account_number = random.randint(1,200)

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.account_number = self.account_number
        self.balance = balance

    def deposite_amoount(self,amount):
        self.balance += amount
        print("Amount Creadited Successfully!")
    
    def withdraw_money(self,amount):
        if amount > self.balance:
            print("Insufficient Amount!")
        else:
            self.balance -= amount
            print("Amount Debited successfully!")
    
    def get_balance(self):
        print(f"Available Balance is: {self.balance}")

    def display_info(self):
        print(f"Name: {self.account_holder} Acc No.: {self.account_number} Balance: {self.balance} ")

account = BankAccount("Alice",5000)
account.display_info()
account.deposite_amoount(4000)
account.withdraw_money(2000)
account.display_info()