"""
Day 9 : Class vs Instance Attributes.
Date: February 23, 2026
Description: Learning different types of Attributes & Methods.

"""

# Example 1: Instance vs Class Attributes.
print("="*50)
print("Example 1: Instance vs Class Attributes.")
print("="*50)

class Employee:

    company = "OwnBrand"
    raise_amount = 1.04

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

emp1 = Employee("Ajay",15000)
emp2 = Employee("Sujal",20000)

print(f"{emp1.name} works at: {Employee.company}")
print(f"{emp2.name} works at: {Employee.company}")

# Different Salaries
print(f"{emp1.name}'s Salary: {emp1.salary}")
print(f"{emp2.name}'s Salary: {emp2.salary}")

# Apply Raise
emp1.apply_raise()
emp2.apply_raise()
print(f"{emp1.name}'s Salary: {emp1.salary}")
print(f"{emp2.name}'s Salary: {emp2.salary}")


# Example 2: Counting Objects
print("\n"+"="*50)
print("Example 2: Counting Objects")
print("="*50)

class Dog:
    total_dogs = 0

    def __init__(self,name):
        self.name = name
        Dog.total_dogs += 1
    
    @classmethod
    def get_total_dogs(cls):
        return cls.total_dogs

print(f"Total Dogs: {Dog.total_dogs}")
dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(f"Total Dogs: {Dog.total_dogs}")

# Example 3: Different Methods Types

print("\n" + "="*50)
print("EXAMPLE 3: Method Types")
print("="*50)

class Pizza:
    # Class attribute
    size_prices = {
        "small": 8,
        "medium": 10,
        "large": 12
    }
    
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
    
    # Instance method - works with specific pizza
    def get_price(self):
        base_price = self.size_prices[self.size]
        topping_price = len(self.toppings) * 1  # $1 per topping
        return base_price + topping_price
    
    # Class method - works with class, not instance
    @classmethod
    def margherita(cls):
        """Factory method to create margherita pizza"""
        return cls("medium", ["cheese", "tomato"])
    
    # Static method - doesn't use class or instance
    @staticmethod
    def is_valid_size(size):
        """Check if size is valid"""
        return size in ["small", "medium", "large"]

# Instance method usage
pizza1 = Pizza("large", ["pepperoni", "mushroom"])
print(f"Pizza price: ${pizza1.get_price()}")

# Class method usage (factory)
pizza2 = Pizza.margherita()
print(f"Margherita price: ${pizza2.get_price()}")

# Static method usage
print(f"Is 'xlarge' valid? {Pizza.is_valid_size('xlarge')}")
print(f"Is 'medium' valid? {Pizza.is_valid_size('medium')}")

