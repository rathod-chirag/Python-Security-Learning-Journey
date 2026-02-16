# Day 1 - Learning Functions
# Date: February 15, 2026

# Example 1: Simple function
def say_hello():
    print("Hello, World!")

say_hello()  # Call the function


# Example 2: Function with parameter
def greet_person(name):
    print(f"Hello, {name}! Welcome to Python!")

greet_person("Rahul")
greet_person("Priya")


# Example 3: Function with return value
def add_numbers(a, b):
    result = a + b
    return result

answer = add_numbers(5, 3)
print(f"5 + 3 = {answer}")


# Example 4: Function with multiple parameters
def introduce(name, age, city):
    print(f"My name is {name}")
    print(f"I am {age} years old")
    print(f"I live in {city}")

introduce("Arjun", 20, "Mumbai")


# Example 5: Function with default parameter
def greet_with_time(name, time="morning"):
    print(f"Good {time}, {name}!")

greet_with_time("Sneha")  # Uses default "morning"
greet_with_time("Amit", "evening")  # Uses "evening"