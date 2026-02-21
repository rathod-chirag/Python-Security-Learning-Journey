"""
Day 2: *args & **kwargs - Learning Examples.
Date: February 16, 2026
Describing: Learninng to  *args & **kwargs.
"""

# *args 

def add_all(*numbers):
    print(f"'numbers' are *args. ")
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    
    print(f"sum of the numbers {numbers} is : {sum}")
    pass

add_all(1,2,3,4,5,6,7,8,9,10)

# **kwargs 

def info(**kwargs):
    print("this function uses kwargs")
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key, value)


info(Name="Chirag", Age=19, Education="Btech",Branch="Information Technology")

def introducee(name, *hobbies, **info):
    print(name)

    print(f"{name}s hobbies are:")
    for i in hobbies:
        print(i)
    
    print(f"{name}s info are:")
    for key, value in info.items():
        print(key, value)

introducee("Chirag", "Editing", "Coding", Age=19, Location="Amravati", Mobile=8945673212)