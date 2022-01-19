class Student:
    __init__(self,name,roll,maths,science,CS):
        self.name = name
        self.roll = roll
        self.maths = maths
        self.science = science
        self.CS = CS

    def calculate(self):
        m = self.maths
        s = self.science
        C = self.CS
        avg = (m+s+c)/2
        return avg
    def display(self):
        avg=self.avg()
        print(f"Name : {self.name}, \n Roll no. : {self.roll}, \n Average marks : {avg}")

    while True:
        

        
        
