#quack.py
"""This module is custom created by siddharth bhattacharjee.
This module is for easier implementation of stacks and queues in python"""
def subjectsList():
    print("There are two classes namely stack and queue")
    print("To declare stack : a_stack = stack() ; [fungtions accociated are isEmpty(),push(),pop(),peek(),display()#prints stack,dect()#returns stack]")
    print("To declare queue : a_queue = queue() ; [fungtions accociated are isEmpty(),enqueue(),dequeue(),peek(),display(),dect()]")
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
    def peek(self):
        if self.isEmpty():
            return "ERROR : STACK UNDERFLOW"
        else:
            item = self.stk[self.top]
            return item
    def display(self):
        if self.isEmpty():
            print("EMPTY STACK")
        else:
            self.top = len(self.stk)-1
            print(self.stk[self.top]," <--- Top")
            for i in range((self.top)-1,-1,-1):
                print(self.stk[i])

    def dect(self):
        if self.isEmpty():
            return "EMPTY STACK"
        else:
            dict_ = {'top_pos' : self.top,'top_ele' : self.stk[self.top], 'stack' : self.stk}
            return dict_
        
            
class queue:
    def __init__(self):
        self.q=[]
        self.rear=len(self.q)-1
        self.front=None

    def isEmpty(self):
        if self.q== []:
            return True
        else:
            return False

    def enqueue(self,item):
        self.q.append(item)
        if len(self.q) == 1:
            self.rere = 0
            self.front = 0
        else:
            self.rere=len(self.q)-1
            self.front = 0

    def dequeue(self):
        if self.isEmpty():
            return "ERROR : QUEUE UNDERFLOW"
        else:
            item = self.q.pop(0)
            if len(self.q) == 0:
                self.rear = None
                self.front = None
            else:
                self.rear = len(self.q)-1
                self.front = 0
            return item
    def peek(self):
        if self.isEmpty():
            return "ERROR : QUEUE UNDERFLOW"
        else:
            self.front=0
            return self.q[self.front]

    def display(self):
        if self.isEmpty():
            print("EMPTY QUEUE")
        elif len(self.q)==1:
            print(self.q[0],"<--- front,rear")
        else:
            self.front=0
            self.rear = len(self.q)-1
            print(self.q[self.front]," <--- front")
            for i in range(1,self.rear):
                print(self.q[i])
            print(self.q[self.rear]," <--- rear")

    def dect(self):
        if self.isEmpty():
            return "EMPTY QUEUE"
        else:
            dict_ = {'front_pos' : self.front,'front_ele' : self.q[self.front],'rear_pos' : self.rear,'rear_ele' : self.q[self.rear] ,'queue' : self.q}
            return dict_
