class students:
    def __init__(self,name,roll,maths,science,cs):
        self.name=name
        self.roll=roll
        self.maths=maths
        self.science=science
        self.cs=cs

    def average(self):
        avg=(self.maths+self.science+self.cs)/3
        return avg

    def display(self):
        x=self.average()
        print(f' Name : {self.name} , \n Roll : {self.roll} , \n Marks : maths - {self.maths}, science - {self.science} , cs - {self.cs} , \n Avg marks : {x}')

class cs_students(students):
    def __init__(self,name,roll,maths,science,cs,language,database):
        super().__init__(name,roll,maths,science,cs)
        self.name=name
        self.roll=roll
        self.maths=maths
        self.science=science
        self.cs=cs
        self.language = language
        self.database = database
        
while True:
    name = input("Enter student name : ")
    roll = int(input("Enter Roll No. : "))
    m = int(input('Enter marks in maths : '))
    s = int(input("Enter marks in science : "))
    c = int(input("Enter marks in CS : "))
    l = input("Enter language : ")
    d = input("Enter Database : ")
    student = cs_students(name,roll,m,s,c,l,d)
    student.display()
        

        
