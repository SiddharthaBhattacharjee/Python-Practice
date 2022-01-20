#static constructor and staticfungtions

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

    @staticmethod
    def isopen(day):
        if day=='sunday':
            return False
        else:
            return True

    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary = emp_string.split('-')
        return cls(fname,lname,salary)

lovish = Employee.from_str('lovish-khanna-76000')
        

harry = Employee('harry','Jackson',44000)
rohan = Employee('Rohan','Das',44000)

print(lovish.fname, lovish.lname, lovish.salary)
