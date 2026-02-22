"""
Day 8 : Introduction to Classe and Obects.
Date: February 22, 2026
Description: Learning OOP Basic  classes, objects, attributes, methods.

"""


# Example 1: Basic class
print("="*50)
print("Example 1: Basic class.")
print("="*50)

# Definig a class
class Dog:
    pass # Empty class.

# creating a objects (instances)
dog_1 = Dog()
dog_2 = Dog()

print(f"dog1 is a: {type(dog_1)}")
print(f"dog2 is a: {type(dog_2)}")
print(f"Are they the objects: {dog_1 is dog_2}")


# Example 2: Class with attributes.

# Adding Attributes
print("\n"+"="*50)
print("Example 2: Attributes")
print("="*50)

class Dog:
    # This is the constructor - runs when object is created  
    def __init__(self,name,age):
        # self.name is an attributes
        self.name = name
        self.age = age
        
dog1 = Dog("Buddy",5)
dog2 = Dog("Max",3)

# Accessing the attributes

print(f"dog1: {dog1.name}, Age: {dog1.age}")
print(f"dog2: {dog2.name}, Age: {dog2.age}")


# Example 3: Adding methods.

# Adding Methods
print("\n"+"="*50)
print("Example 3: Methods")
print("="*50)

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    # This is a method (function inside class)

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

    def get_info(self):
        return f"{self.name} is {self.age} years old."

dog1 = Dog("Buddy",5)
dog1.bark() # Call Method
print(dog1.get_info()) # Call method that returns value


# Example 4: Multiple Objects.

# Multiple Objects
print("\n"+"="*50)
print("Example 4: Multiple Objects")
print("="*50)

class Dog:
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

    def birthday(self):
        self.age += 1
        print("Happy Birthday {self.name}! Now {self.age} years old!")

Dogs = [Dog("Buddy",5,"Golden Retriever"),Dog("Max",3,"German Shepherd"),Dog("Charlie",2,"Labrador")]

for dog in Dogs:
    print(f"{dog.name} ({dog.breed})")
    dog.bark()
    print()