""" 
Day 1 : Functions & Parameters - Exercise.
Date: February 15, 2026
Description: Built calculator and tempereture converter. 
"""

# Exercise 1: Temperature Converter
def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5 ) + 32
    return fahrenheit

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius

print("Temprature Convertor.")
print("=" * 30)

# Test 1
temp_c = 25
temp_f = celcius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

# Test 2
temp_f = 77
temp_c = fahrenheit_to_celcius(temp_f)
print(f"{temp_f}°F = {temp_c}°C")

print("Choose the operation you want to  do.")
print("""Enter 1 to convert 'celcius_to_fahrenheit'.
2 to convert 'fahrenheit_to_celcius' """)

choice = int(input("Enter 1 or 2 : "))

if choice  == 1:
    temp_c = float(input("Enter the celcius: "))
    temp_f = celcius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C = {temp_f}°F")
elif choice == 2:
    temp_f = float(input("Enter the Fahrenheit: "))
    temp_c = fahrenheit_to_celcius(temp_f)
    print(f"{temp_f}°F = {temp_c}°C")
else:
    print("Enter the Valid input.")


# Exercise 2: Simple Calculator with Functions

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Number can't divide by 0 ."
    
    return a/b

def calculator():
    """Main calculator function"""
    print("\n"+"="*40)
    print("     SIMPLE CALCULATOR")
    print("="*40)
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("="*40)

    # Choosing the Operation.
    choice = int(input("Enter the number of the operation from 1 to 4:"))
    
    # taking the numbers.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        result = add(num1,num2)
        print(f"Addition of {num1} + {num2} = {result}")
    elif choice == 2:
        result = subtract(num1,num2)
        print(f"Subtraction of {num1} - {num2} = {result}")
    elif choice == 3:
        result = multiply(num1,num2)
        print(f"Multiplication of {num1} - {num2} = {result}")
    elif choice == 4:
        result = divide(num1,num2)
        print(f"Division of {num1} - {num2} = {result}")
    else:
        print("Invalide Input")

calculator()


# Exercise 3 Number checker.

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 !=0

def is_positive(num):
    return num > 0

def is_negative(num):
    return num < 0

def check_number(num):
    """Check all properties of a number"""
    print(f"\nNumber : {num}")
    print(f"Even: {is_even(num)}")
    print(f"Odd: {is_odd(num)}")
    print(f"Positive: {is_positive(num)}")
    print(f"Negative: {is_negative(num)}")

# Test
print("\n"+"="*40)
print("   Check Number ")
print("="*40)
number = int(input("Enter the number: "))
check_number(number)