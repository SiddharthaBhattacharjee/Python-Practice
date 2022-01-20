class Employee:
    
    increment = 1.5
    
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    def increament(self):
        self.increase()
        print(self.salary)

harry = Employee('Harry','Jackson',44000)
rohan = Employee('Rohan','Das',44000)

print(harry.salary)
harry.increase()
print(harry.salary)

harry.increament()
