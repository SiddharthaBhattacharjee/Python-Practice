import csv
class Employee:
    domain = "@silph.co.in"
    def __init__(self,name,exp,age,salary):
        domain = "@silph.co.in"
        self.name = name
        self.exp = exp
        self.age = age
        self.salary = salary
        self.email = name+domain

    def increment(self):
        self.salary = self.salary *1.5

    def exp_add(self):
        self.exp += 1

    def upd_age(self):
        self.age += 1

    def entry(self):
        a_file = open("data.csv",'w')
        dic = self.__dict__
        writer = csv.writer(a_file)
        for key,value in dic.items():
            writer.writerow([key,value])
        a_file.close()

    @staticmethod
    def work_day(day):
        if day == "Sunday" or day == "Saturday":
            return "Closed"
        else:
            return "Workday"

    def increase(self,val):
        self.increment += val

    @classmethod
    def change_domain(dom):
        cls.domain = "@"+dom

class Programmer(Employee):
    def __init__(self,name,exp,age,salary,language,db):
        super().__init__(name,exp,age,salary)
        self.language = language
        self.db = db

    def change_lan(self,lan):
        self.language = lan

    def change_db(self,db):
        self.db = db

class analatic(Employee):
    def __init__(self,name,exp,age,salary,db,department):
        super().__init__(name,exp,age,salary)
        self.db = db
        self.department = department

    def change_db(self,db):
        self.db = db

    def change_dept(dept):
        self.department = dept




        
        
    

    
        
