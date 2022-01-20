# Defining a fungtion to update value of a class variable

class Employee:
    increment = 1.5
    no_of_employees = 0

    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1

    def increase(self):
        self.salary = int(self.salary * Employee.increment)
        
    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount

harry = Employee('harry','Jackson',44000)
rohan = Employee('Rohan','Das',44000)

print(harry.salary)
harry.increase()
print(harry.salary)

print(rohan.salary)
Employee.change_increment(1.7)
rohan.increase()
print(rohan.salary)

