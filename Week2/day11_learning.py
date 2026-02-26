"""
Day 11: Inheritance - Parent & child classes.
Date: February 26, 2026
Description: Learning to  create class hierarchies.

"""

# Example 1: Basic Inheritance 
print("="*50)
print("Example 1: Basic Inheritance ")
print("="*50)

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Employee: {self.name}")
        print(f"Salary: {self.salary}")
    
    def work(self):
        print(f"{self.name} is working.")

class Manager(Employee):
    pass

emp = Employee("Aman",18000)
emp.display_info()
emp.work()

mgr = Manager("Atul",14000)
mgr.display_info()
mgr.work()


# Example 2: Adding New Methods to child. 
print("="*50)
print("Example 2: Adding New Methods to child.")
print("="*50)

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Employee: {self.name}")
        print(f"Salary: {self.salary}")
    
    def work(self):
        print(f"{self.name} is working.")

class Manager(Employee):
    def hold_meeting(self):
        print(f"{self.name} is holding a meeting.")
    
class Developer(Employee):

    def write_code(self):
        print(f"{self.name} is writing code.")


mgr = Manager("Atul",14000)
mgr.display_info()
mgr.work()
mgr.hold_meeting()

dev = Developer("Sujal",25000)
dev.display_info()
dev.work()
dev.write_code()


# Example 3: Method Overriding 
print("="*50)
print("Example 3: Method Overriding.")
print("="*50)

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    # Overriding the method speak.
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):

    # Overriding the method speak.
    def speak(self):
        print(f"{self.name} says Meow!")


animal = Animal("Generic Animal")
animal.speak()

dog = Dog("Buddy")
dog.speak()

cat = Cat("Whiskers")
cat.speak()


# Example 4: Using super()
print("\n" + "="*50)
print("EXAMPLE 4: Using super()")
print("="*50)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Vehicle created: {brand} {model}")
    
    def start(self):
        print(f"{self.brand} {self.model} is starting")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        # Call parent's __init__ using super()
        super().__init__(brand, model)
        
        # Add child's own attribute
        self.doors = doors
        print(f"Car has {doors} doors")
    
    def start(self):
        # Call parent's start method
        super().start()
        
        # Add child's own behavior
        print("Car is ready to drive!")

# Test
car = Car("Toyota", "Camry", 4)
print()
car.start()



# Example 5: Multiple Levels of Inheritance
print("\n" + "="*50)
print("EXAMPLE 5: Multi-Level Inheritance")
print("="*50)

class LivingThing:
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print(f"{self.name} is breathing")

class Animal(LivingThing):  # Animal inherits from LivingThing
    def move(self):
        print(f"{self.name} is moving")

class Dog(Animal):  # Dog inherits from Animal (which inherits from LivingThing)
    def bark(self):
        print(f"{self.name} says Woof!")

# Test
dog = Dog("Max")
dog.breathe()  # From LivingThing
dog.move()     # From Animal
dog.bark()     # From Dog

# Hierarchy:
# LivingThing
#     ↓
#   Animal
#     ↓
#    Dog


# Example 6: isinstance() and issubclass()
print("\n" + "="*50)
print("EXAMPLE 6: Checking Relationships")
print("="*50)

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

# isinstance - check if object is instance of class
print(f"dog is instance of Dog? {isinstance(dog, Dog)}")      # True
print(f"dog is instance of Animal? {isinstance(dog, Animal)}")  # True (inherited!)
print(f"dog is instance of str? {isinstance(dog, str)}")      # False

# issubclass - check if class inherits from another
print(f"Dog is subclass of Animal? {issubclass(Dog, Animal)}")  
print(f"Animal is subclass of Dog? {issubclass(Animal, Dog)}")  
