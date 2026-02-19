# Day 5 - Learning Exception Handling 
# Date - 19-frb-2026

print("="*40)
print("Day 5: exception handlin.")
print("="*40)

#  Example 1 :
# without handling.

def divide_without_handling():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    result = int(a) / int(b)
    print(result)


# Example 2 :
# using try and except block.

def divide_with_handling():
   
    try:
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        result = int(a) / int(b)
        print(result)
    except ValueError:
        print("Please enter integer only.")
    except ZeroDivisionError:
        print("Cannot divided by zero.")
    

# Example 3 :
# try-except-else-finally.

def complete_structure():
    try:
        a = input("Enter the number: ") 
        result = 100 / int(a)
    except ValueError:
        print("Enter only integer number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(result)
    finally:
        print("Thanks!")

# divide_without_handling()
# divide_with_handling()
# complete_structure()

# file reading:
def read_file(filename):
    try:
        with open(filename,'r') as f:
            data = f.read()
    except FileNotFoundError:
        print("File Not Found!")

# read_file('missing.txt')

# Raising Exception:

def check_age(age):
    if age < 0 :
        raise ValueError("Age cannot be negative.")
    elif age > 150 :
        raise ValueError("Not Valide age.")
    else:
        print("Valid age.")

try:
    check_age(164)
except ValueError as e:
    print(f"Error: {e}")