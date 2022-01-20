#static constructor and staticfungtions

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

        
        

harry = Employee('harry','Jackson',44000)
rohan = Employee('Rohan','Das',44000)

class Programmer(Employee):
    def __init__(self,fname,lname,salary,proglang,exp):
        super().__init__(fname,lname,salary)
        self.proglang = proglang
        self.exp = exp

    def increase(self):
        self.salary = int(self.salary * (self.increment+2))

sid = Programmer('Siddharth' , 'Bhattacharjee' , 44000 , 'Python' , '2 yrs')
print(sid.fname,sid.proglang)

harry.increase()
sid.increase()

print(harry.salary)
print(sid.salary)
