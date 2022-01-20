#This is class variable
class Employee:
    no_of_employee = 0
    increment = 1.5
    
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1

    def increase(self):
        self.salary = int(self.salary * Employee.increment)

harry = Employee('Harry','Jackson',44000)
rohan = Employee('Rohan','Das',44000)

print(Employee.no_of_employee)

shital = Employee('Shital','Gupta',44000)

print(Employee.no_of_employee)
