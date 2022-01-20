class Employee:

    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.5

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return "Employee ({} , {} , {})".format(self.fname,self.lname,self.salary)

    def __str__(self):
        return 'The Employee is {}'.format(self.fname)


        
        

harry = Employee('harry','Jackson',44000)
rohan = Employee('rohan','Das',44000)

print(harry+rohan)

print(repr(harry))

print(str(harry))
print(harry)
