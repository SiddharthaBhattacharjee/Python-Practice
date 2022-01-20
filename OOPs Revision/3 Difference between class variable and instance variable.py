#This is class variable
class Employee:
    
    increment = 1.5#class variable
    
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * Employee.increment)

harry = Employee('Harry','Jackson',44000)
rohan = Employee('Rohan','Das',44000)

print(harry.salary)
harry.increase()
print(harry.salary)


#This is instance variable or constructor variable
class Employee:
    increment=1.5 #just for verification... Not used by code
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment=1.4#constructor variable

    def increase(self):
        self.salary = int(self.salary * self.increment)

harry = Employee('Harry','Jackson',44000)
rohan = Employee('Rohan','Das',44000)

print(harry.salary)
harry.increase()
print(harry.salary)
