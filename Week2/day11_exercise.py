"""
Day 11: Inheritance - Parent & child classes - Exercise.
Date: February 26, 2026
Description: Building Employee management system.

"""
print("="*50)
print("Exercise 1: Employee management system.")
print("="*50)

class Employee:

    def __init__(self,name,emp_id,salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def dispaly_info(self):
        print(f"{self.name} is Employee.")
        print(f"Monthly salary is : ${self.salary}")

    def work(self):
        print(f"{self.name} is working.")

    def get_annual_salary(self):
        print(f"Annual Salary of {self.name} is ${self.salary*12}")
    

class Manager(Employee):

    def __init__(self, name, emp_id, salary,team_size):
        super().__init__(name, emp_id, salary)

        self.team_size = team_size

    def conduct_meeting(self):
        print(f"{self.name} conducts meetings!")
    
    def work(self):
        print(f"{self.name} working and managing a team.")

class Developer(Employee):

    def __init__(self, name, emp_id, salary,programming_lng):
        super().__init__(name, emp_id, salary)

        self.programming_lng = programming_lng
    
    def write_code(self):
        print(f"{self.name} write a codes!")

    def work(self):
        print(f"{self.name} work with {self.programming_lng}")

class Intern(Employee):

    def __init__(self, name, emp_id, salary,university):
        super().__init__(name, emp_id, salary)

        self.university = university

    def learn(self):
        print(f"{self.name} is learning the job.")

    def get_annual_salary(self):
        return super().get_annual_salary()
    
emp = Employee("Samir",102,12500)
emp.dispaly_info()
emp.work()
emp.get_annual_salary()

mng = Manager("Naman",102,25000,14)
mng.dispaly_info()
mng.work()
mng.conduct_meeting()
mng.get_annual_salary()

dev = Developer("Soham",102,20000,"Python")
dev.dispaly_info()
dev.work()
dev.write_code()
dev.get_annual_salary()

intr = Intern("Ramesh",102,10000,"Galgotiya")
intr.dispaly_info()
intr.work()
intr.learn()
intr.get_annual_salary()


print("="*50)
print("Exercise 2: Vehical System.")
print("="*50)

class Vehical:

    def __init__(self,brand,model,year,price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price 

    def start(self):
        print(f"{self.brand}'s vehical is started.")

    def stop(self):
        print(f"{self.brand}'s vehical is stoped.")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"price: {self.price}")

    def calculate_age(self):
        return 2026 - self.year
    
class Car(Vehical):

    def __init__(self, brand, model, year, price,doors,fuel_type):
        super().__init__(brand, model, year, price)
        self.doors = doors
        self.fuel_type = fuel_type
    
    def start(self):
        print("Car engine is starting!")

    def open_trunk(self):
        print("Opening a trunk!")


class  Motercycle(Vehical):

    def __init__(self, brand, model, year, price,has_sidecar):
        super().__init__(brand, model, year, price)
        self.has_sidecar = has_sidecar

    def start(self):
        print("MoterCycle enging starts!")

    def wheelie(self):
        print("Motercycle can do wheelie!")
    
class Truck(Vehical):

    def __init__(self, brand, model, year, price,cargo_capacity,is_loaded):
        super().__init__(brand, model, year, price)
        self.cargo_capacity = cargo_capacity
        self.is_loaded = is_loaded

    def start(self):

        if self.is_loaded:
            print("Truck engine starts.")


class ElectricCar(Vehical):

    def __init__(self, brand, model, year, price,battery_capacity):
        super().__init__(brand, model, year, price)
        self.battery_capacity = battery_capacity

    def start(self):
        print("Electric Car starts, and does't make noice.")

    def charge_battery(self):
        print("Electric Car is on charging. ")

veh = Vehical("BMW","M5",2022,"1.7cr")
veh.display_info()
veh.start()
veh.stop()
print(f"{veh.calculate_age()} years old")

car = Car("BMW","M8",2024,"2.3cr","2 doors","petrol")
car.display_info()
car.start()
car.stop()
car.open_trunk()
print(f"{car.calculate_age()} years old")

moter = Motercycle("BMW","s1000r",2026,"35 lacks",False)
moter.display_info()
moter.start()
moter.stop()
moter.wheelie()
print(f"{moter.calculate_age()} years old")

truck = Truck("Tata","Tata s1",2026,"2.3cr","25 tons",True)
truck.display_info()
truck.start()
truck.stop()
print(f"{truck.calculate_age()} years old")

ele = ElectricCar("Tata","Siara",2026,"15 lacks","200 km")
ele.display_info()
ele.start()
ele.stop()
ele.charge_battery()
print(f"{ele.calculate_age()} years old")



print("="*50)
print("Exercise 3: BankAccount System.")
print("="*50)

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance   # protected variable

    def get_balance(self):
        print(f"Balance: {self._balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
        else:
            self._balance += amount
            print(f"Deposited: {amount}")

    def withdrawal(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
        elif amount > self._balance:
            print("Insufficient Balance!")
        else:
            self._balance -= amount
            print(f"Withdrawal: {amount}")
            print(f"Remaining Balance: {self._balance}")


# ---------------- SAVINGS ACCOUNT ----------------
class SavingAccount(BankAccount):

    withdrawal_count = 0
    MAX_WITHDRAWALS = 3

    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print("Interest added successfully!")
        print(f"New Balance: {self._balance}")

    def withdrawal(self, amount):
        if SavingAccount.withdrawal_count < SavingAccount.MAX_WITHDRAWALS:
            SavingAccount.withdrawal_count += 1
            super().withdrawal(amount)
        else:
            print("You have crossed the monthly withdrawal limit.")


# ---------------- CHECKING ACCOUNT ----------------
class CheckingAccount(BankAccount):

    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdrawal(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
        elif amount > self._balance + self.overdraft_limit:
            print("Overdraft limit exceeded!")
        else:
            self._balance -= amount
            print(f"Withdrawal: {amount}")
            print(f"Remaining Balance: {self._balance}")

    def check_overdraft_available(self):
        print(f"Overdraft limit available: {self.overdraft_limit}")


# ---------------- STUDENT ACCOUNT ----------------
class StudentAccount(BankAccount):

    def __init__(self, owner, balance, student_id, university):
        super().__init__(owner, balance)
        self.student_id = student_id
        self.university = university

    def deposit(self, amount):
        if amount > 100:
            print("Bonus obtained!")
        super().deposit(amount)

    def verify_student(self):
        print("Student verified successfully.")


# ---------------- TESTING ----------------
acc = BankAccount("Alice", 12000)
acc.get_balance()
acc.deposit(2000)
acc.withdrawal(5000)

print("\n--- Saving Account ---")
svacc = SavingAccount("Alice", 12000, 0.05)
svacc.get_balance()
svacc.deposit(2000)
svacc.withdrawal(2000)
svacc.withdrawal(1000)
svacc.withdrawal(500)
svacc.withdrawal(300)
svacc.add_interest()

print("\n--- Checking Account ---")
ckacc = CheckingAccount("Alice", 12000, 3000)
ckacc.get_balance()
ckacc.deposit(2000)
ckacc.withdrawal(15000)
ckacc.check_overdraft_available()

print("\n--- Student Account ---")
stdacc = StudentAccount("Alice", 12000, 123, "Galgotias")
stdacc.get_balance()
stdacc.deposit(2000)
stdacc.withdrawal(5000)
stdacc.verify_student()