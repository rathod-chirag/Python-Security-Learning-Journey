"""
Day 5: Exception Handling - Exercises.
Date: February 19, 2026
Describing: Built Safe Calculator and file handler with error handling.
"""

# Exercise 1 - Safe Calculator.

def safe_calculator():
    while True:
        try:
            print("\n === Safe Calculator ===")
            print("="*40)
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")

            

            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            choice = int(input("Enter a number form the 1-5: "))
            
            if choice == 1:
                result = a + b
                print(f"Sum of {a} + {b} is : {result}")
            elif choice == 2:
                result = a - b
                print(f"Diff of {a} - {b} is : {result}")
            elif choice == 3:
                result = a * b
                print(f"Product of {a} * {b} is : {result}")
            elif choice == 4:
                result = a / b
                print(f"Result of {a} / {b} is : {result}")
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid Choice!")
            
        except ValueError:
            print("Please enter valide number.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        except Exception as  e:
            print(f"Error: {e}")

safe_calculator()

# Exercise 2 - File Operation.

def safe_read(filename):
    try:
        with open(filename,'r') as f:
            data = f.read()
            print(data)
            return data
    except FileNotFoundError:
        print("File Not Found.")
        return
    except PermissionError:
        print("NO Permission ! ")
        return
    
safe_read('contact.txt')
safe_read('missing.txt')

def safe_write(filename,content):
    try:
        with open(filename,'w') as f:
            f.write(content)
            print("File saved!")
    except PermissionError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print("Error: {e}")
        return False
    
safe_write('sample.txt')

def safe_file_operation():
    while True:
        print("1. Read File")
        print("2. Write File")
        print("4. Exit")

        choice = int(input("Enter the nuumber (1-3): "))

        if choice == 1:
            file = input("enter filename.")
            safe_read(file)
        elif choice == 2:
            filename = input("Enter the file name: ")
            content = input("Enter the content to write in the file: ")
            safe_write(filename,content)
        elif choice == 3:
            print("Thanks!")
            break
        else: 
            print("Invalide Input.")


safe_file_operation()