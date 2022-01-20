class Employee:

    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.5
        self.efn = self.fname
        self.eln = self.lname

    def increase(self):
        self.salary = int(self.salary * self.increment)
    @property
    def email(self):
        if self.efn==None or self.eln==None:
            return "Email Not Found"
        else:

            return self.efn + '_' + self.eln + '@gmail.com'

    @email.setter
    def email(self, given_email):

        name_list = given_email.split('@')[0].split('_')
        self.efn = name_list[0]
        self.eln = name_list[1]

    @email.deleter
    def email(self):
        self.efn = None
        self.eln = None

    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount

    


        
if __name__ == "__main__":
        
    harry = Employee('harry','jackson',99000)
    rohan = Employee('rohan','agarwal',9)
    print(harry.email , rohan.email)
    rohan.lname = 'khanna'
    print(rohan.email)
    rohan.email = 'khanna_rohan@gmail.com'
    print(rohan.email)
    print(rohan.fname)
    del rohan.email
    print(rohan.email)
