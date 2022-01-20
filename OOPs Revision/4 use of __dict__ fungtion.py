#This is class variable
class Employee:
    
    increment = 1.5
    
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * Employee.increment)

harry = Employee('Harry','Jackson',44000)
rohan = Employee('Rohan','Das',44000)

print(harry.__dict__)
harry.weight='72Kg'
print(harry.__dict__)

print(Employee.__dict__)
