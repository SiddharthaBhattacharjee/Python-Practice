class stack:
    def __init__(self):
        self.stk=[]
        self.top=len(self.stk)-1

    def isEmpty(self):
        if self.stk== []:
            return True
        else:
            return False

    def push(self,item):
        self.stk.append(item)
        self.top=len(self.stk)-1

    def pop(self):
        if self.isEmpty():
            return "ERROR : STACK UNDERFLOW"
        else:
            item = self.stk.pop()
            if len(self.stk) == 0:
                self.top = None
            else:
                self.top = len(self.stk)-1
            return item
        
    def display(self):
        if self.isEmpty():
            print("EMPTY STACK")
        else:
            self.top = len(self.stk)-1
            print(self.stk[self.top]," <--- Top")
            for i in range((self.top)-1,-1,-1):
                print(self.stk[i])

def isPelindrome(st):
    y=st
    s=stack()
    for i in y:
        s.push(i)

    z=""
    for i in range(len(y)):
        x=s.pop()
        z=z+str(x)

    if y==z:
        return "Pelindrome"
    else:
        return "Not Pelindrome"

if __name__ == "__main__":
    word = str(input("Enter a string : "))
    p = isPelindrome(word)
    print(f"The Entered string '{word}' is a {p}")
        
        
