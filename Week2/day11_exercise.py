"""
Day 11: Inheritance - Parent & child classes - Exercise.
Date: February 26, 2026
Description: Building Employee management system.

"""

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