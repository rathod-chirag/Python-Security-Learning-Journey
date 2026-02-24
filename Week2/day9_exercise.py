"""
Day 9 : Class vs Instance Attributes - Exercise.
Date: February 23, 2026
Description: Creating a classes.

"""
# Exercise 1: Car Dealership

print("="*50)
print("Car Dealership:")
print("="*50)

class CarDealership:
    total_cars = 0
    sold_cars = 0
    manufacture = "AutoMaker Inc."

    def __init__(self,model,color,price):
        self.model = model
        self.color = color
        self.price = price
        self.is_sold = False
        CarDealership.total_cars += 1
    
    def display_info(self):
        print(f"Model: {self.model}, Color: {self.color}, Price: {self.price}, Manufacture: {CarDealership.manufacture},Sold: {self.is_sold}")

    def sell(self):
        CarDealership.sold_cars += 1
        self.is_sold = True
    
    def apply_discount(self,percentage):
        discount = (self.price * percentage) / 100
        return discount
    
    @classmethod
    def get_total_cars(cls):
        return cls(CarDealership.total_cars) 
    
    @classmethod
    def get_unsold_cars(cls):
        unsold = CarDealership.total_cars - CarDealership.sold_cars
        return unsold
    
    @staticmethod
    def is_valid_color(color):
        return color in ["red","blue","black","white","silver"]
    

car1 = CarDealership("Sedan","blue",25000)
car2 = CarDealership("SUV","red",35000)
car3 = CarDealership("Truck","black",40000)

print(f"Total Cars: {CarDealership.total_cars}")

car1.display_info()
print(car1.apply_discount(10))
car1.sell()

print(f"Unsold Cars: {CarDealership.get_unsold_cars()}")

print(CarDealership.is_valid_color("green"))
print(CarDealership.is_valid_color("blue"))
    
# Exercise 2: Restaurent System

print("="*50)
print("Restaurent System:")
print("="*50)

class Restaurant:
    # Class attributes
    restaurant_name = "Python Cafe"
    menu = {
        "pizza": 12,
        "burger": 8,
        "pasta": 10,
        "salad": 6
    }
    total_orders = 0

    def __init__(self,table_number):
        self.table_number = table_number
        self.order_items = []
        self.order_total = 0
    
    def add_item(self,item):
        """Add item to order"""
        
        # Check if item exists in menu
        if item not in self.menu:
            print(f"❌ Sorry, '{item}' is not on the menu!")
            return
        
        # Get price from menu (class attribute)
        price = self.menu[item]
        
        # Add to order
        self.order_items.append(item)
        self.order_total += price
        
        print(f"✅ Added {item} (${price}) to Table {self.table_number}")

    def remove_item(self,item):
        """Remove item from order"""
        
        # Check if item is in the order
        if item not in self.order_items:
            print(f"❌ '{item}' is not in your order!")
            return
        
        # Get price
        price = self.menu[item]
        
        # Remove from order
        self.order_items.remove(item)  # Removes first occurrence
        self.order_total -= price
        
        print(f"🗑️  Removed {item} (${price}) from Table {self.table_number}")

    def display_order(self):
        """Show current order"""
        print("\n" + "="*40)
        print(f"📋 {self.restaurant_name}")
        print(f"   Table {self.table_number}")
        print("="*40)
        
        if not self.order_items:
            print("   No items ordered yet")
            print("="*40)
            return
        
        # Show each item with price
        for item in self.order_items:
            price = self.menu[item]
            print(f"   {item.capitalize():<15} ${price:>5}")
        
        print("-"*40)
        print(f"   {'TOTAL':<15} ${self.order_total:>5}")
        print("="*40)
        
    def finalize_order(self):
        """Complete and print receipt"""
        
        if not self.order_items:
            print("❌ Cannot finalize empty order!")
            return
        
        # Increment class attribute
        Restaurant.total_orders += 1
        
        # Print receipt
        print("\n" + "="*40)
        print("🧾 RECEIPT")
        print("="*40)
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Table: {self.table_number}")
        print(f"Order #{Restaurant.total_orders}")
        print("-"*40)
        
        for item in self.order_items:
            price = self.menu[item]
            print(f"{item.capitalize():<15} ${price:>5}")
        
        print("-"*40)
        print(f"{'TOTAL':<15} ${self.order_total:>5}")
        print("="*40)
        print("Thank you! 😊")

    @classmethod
    def add_menu_item(cls, item, price):
        """Add new item to menu"""
        cls.menu[item] = price
        print(f"✅ Added '{item}' to menu at ${price}")
    
    @classmethod
    def get_total_orders(cls):
        """Return total orders made"""
        return cls.total_orders
    
    @classmethod
    def display_menu(cls):
        """Show all menu items"""
        print("\n" + "="*40)
        print(f"📖 {cls.restaurant_name} MENU")
        print("="*40)
        
        for item, price in cls.menu.items():
            print(f"{item.capitalize():<15} ${price:>5}")
        
        print("="*40)
    
    @staticmethod
    def calculate_tip(total, percentage):
        """Calculate tip amount"""
        tip = total * (percentage / 100)
        return tip

if __name__ == "__main__":
    # Show menu
    Restaurant.display_menu()
    
    # Table 5's order
    order1 = Restaurant(5)
    order1.add_item("pizza")
    order1.add_item("burger")
    order1.display_order()
    
    # Calculate tip
    tip = Restaurant.calculate_tip(order1.order_total, 15)
    print(f"\n💵 Suggested tip (15%): ${tip:.2f}")
    
    # Finalize
    order1.finalize_order()
    
    # Table 3's order
    order2 = Restaurant(3)
    order2.add_item("pasta")
    order2.finalize_order()
    
    print(f"\n📊 Total orders today: {Restaurant.get_total_orders()}")

# class Student:

print("="*50)
print("Student Management:")
print("="*50)

# class Student:

class Student:
    # Class attributes
    school_name = "Python High School"
    total_students = 0
    all_students = []  # Store all student objects
    passing_grade = 50

    def __init__(self, name, age, grade):
        # Instance attributes
        self.name = name
        self.age = age
        self.grade = grade
        
        # Update class attributes
        Student.total_students += 1
        Student.all_students.append(self)  # Add THIS student to list
    
    @classmethod
    def get_class_average(cls):
        """Calculate average grade of all students"""
        
        # Check if any students exist
        if not cls.all_students:
            return 0
        
        # Sum all grades
        total_grade = 0
        for student in cls.all_students:
            total_grade += student.grade
        
        # Calculate average
        average = total_grade / len(cls.all_students)
        return average
    
    @classmethod
    def get_top_student(cls):
        """Return student with highest grade"""
        
        if not cls.all_students:
            return None
        
        # Start with first student as top
        top_student = cls.all_students[0]
        
        # Check each student
        for student in cls.all_students:
            if student.grade > top_student.grade:
                top_student = student
        
        return top_student
    
    @classmethod
    def get_passing_students(cls):
        """Return list of passing students"""
        
        passing = []
        
        for student in cls.all_students:
            if student.grade >= cls.passing_grade:
                passing.append(student)
        
        return passing
    
    @staticmethod
    def grade_to_gpa(grade):
        """Convert grade (0-100) to GPA (0.0-4.0)"""
        
        if grade >= 90:
            return 4.0
        elif grade >= 80:
            return 3.0
        elif grade >= 70:
            return 2.0
        elif grade >= 60:
            return 1.0
        else:
            return 0.0
        

# Create students
s1 = Student("Aman", 20, 92)
s2 = Student("Badal", 21, 78)
s3 = Student("Chetan", 19, 45)
s4 = Student("Dinesh", 22, 88)
    
# Class info
print(f"School: {Student.school_name}")
print(f"Total students: {Student.total_students}")
print(f"Class average: {Student.get_class_average():.2f}")
    
# Top student
top = Student.get_top_student()
print(f"\nTop student: {top.name} with grade {top.grade}")
    
# Passing students
passing = Student.get_passing_students()
print(f"\nPassing students ({len(passing)}):")
for student in passing:
    print(f"  - {student.name}: {student.grade}")
