from tkinter import *
import tkinter
    
root=Tk()
root.title("Sid's Calculator")
root.configure(bg='Gray65')
root.geometry("256x490+370+220")

data = StringVar()
val = ""
A = 0
temp=0
operator = ''


def back():
    global val
    val = val[:-1]
    data.set(val)
    
def btn_1_clk():
    global val
    val=val+'1'
    data.set(val)
    
def btn_2_clk():
    global val
    val=val+'2'
    data.set(val)

def btn_3_clk():
    global val
    val=val+'3'
    data.set(val)

def btn_4_clk():
    global val
    val=val+'4'
    data.set(val)

def btn_5_clk():
    global val
    val=val+'5'
    data.set(val)

def btn_6_clk():
    global val
    val=val+'6'
    data.set(val)

def btn_7_clk():
    global val
    val=val+'7'
    data.set(val)

def btn_8_clk():
    global val
    val=val+'8'
    data.set(val)

def btn_9_clk():
    global val
    val=val+'9'
    data.set(val)

def btn_0_clk():
    global val
    val=val+'0'
    data.set(val)

def sq():
    global A
    global operator
    global val
    operator='^'
    A=float(val)
    val=val+'^'
    data.set(val)


def decimal_clk():
    global val
    if '.' in val and '+' not in val and '-' not in val and '*' not in val and '/' not in val and '^' not in val:
        exit
    elif '+' in val:
        val2=val
        h = (val2.split('+')[1])
        if '.' in h:
            exit
        else:
            val=val+'.'
            data.set(val)
            
    elif '-' in val:
        val2=val
        h = (val2.split('-')[1])
        if '.' in h:
            exit
        else:
            val=val+'.'
            data.set(val)
    elif '*' in val:
        val2=val
        h = (val2.split('*')[1])
        if '.' in h:
            exit
        else:
            val=val+'.'
            data.set(val)
    elif '/' in val:
        val2=val
        h = (val2.split('/')[1])
        if '.' in h:
            exit
        else:
            val=val+'.'
            data.set(val)

    elif '^' in val:
        val2=val
        h = (val2.split('^')[1])
        if '.' in h:
            exit
        else:
            val=val+'.'
            data.set(val)

    else:
        val=val+'.'
        data.set(val)

    

def btn_plus_clk():
    global A
    global operator
    global val
    A = float(val)
    operator = '+'
    val = val + '+'
    data.set(val)

def btn_minus_clk():
    global A
    global operator
    global val
    A = float(val)
    operator = '-'
    val = val + '-'
    data.set(val)

def btn_multiply_clk():
    global A
    global operator
    global val
    A = float(val)
    operator = '*'
    val = val + '*'
    data.set(val)

def btn_devide_clk():
    global A
    global operator
    global val
    A = float(val)
    operator = '/'
    val = val + '/'
    data.set(val)

def sqrt():
    global val
    x = float(val)
    C = x**(1/2)
    C = float("{:.5f}".format(C))
    data.set(C)
    val = str(C)

def C_clk():
    global A
    global operator
    global val
    val=''
    operator=''
    A=0
    data.set(val)

def result():
    global A
    global operator
    global val
    val2 = val
    if operator == '+':
        x = float((val2.split('+')[1]))
        C = A + x
        data.set(C)
        val = str(C)
    if operator == '-':
        x = float((val2.split('-')[1]))
        C = A - x
        data.set(C)
        val = str(C)
    if operator == '*':
        x = float((val2.split('*')[1]))
        C = A * x
        data.set(C)
        val = str(C)
    if operator == '/':
        x = float((val2.split('/')[1]))
        if x==0:
            val = val[:-1]
            data.set(val)
        else:    
            C = A/x
            C = float("{:.5f}".format(C))
            data.set(C)
            val = str(C)
    if operator == '^':
        x = float((val2.split('^')[1]))
        C = A**x
        data.set(C)
        val = str(C)
        
text= Label(root,text='Label',bd=5,anchor = SE, font=("Verdana",20),relief=RIDGE,textvariable=data)
text.pack(expand=True, fill='both')

fm_2=Frame(root,width=300,height=400,bd=10,relief=RIDGE,bg='gray65')
fm_2.pack(expand=True, fill=X)

B1 = Button(fm_2,text='1',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_1_clk)
B1.grid(row=4,column=0)
B2 = Button(fm_2,text='2',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_2_clk)
B2.grid(row=4,column=1)
B3 = Button(fm_2,text='3',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_3_clk)
B3.grid(row=4,column=2)
B4 = Button(fm_2,text='4',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_4_clk)
B4.grid(row=3,column=0)
B5 = Button(fm_2,text='5',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_5_clk)
B5.grid(row=3,column=1)
B6 = Button(fm_2,text='6',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_6_clk)
B6.grid(row=3,column=2)
B7 = Button(fm_2,text='7',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_7_clk)
B7.grid(row=2,column=0)
B8 = Button(fm_2,text='8',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_8_clk)
B8.grid(row=2,column=1)
B9 = Button(fm_2,text='9',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_9_clk)
B9.grid(row=2,column=2)
B0 = Button(fm_2,text='0',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_0_clk)
B0.grid(row=5,column=0)

Bm = Button(fm_2,text='*',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_multiply_clk)
Bm.grid(row=5,column=1)
Bp = Button(fm_2,text='.',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=decimal_clk)
Bp.grid(row=5,column=2)
Be = Button(fm_2,text='=',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=result)
Be.grid(row=5,column=3)
Bd = Button(fm_2,text='/',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_devide_clk)
Bd.grid(row=4,column=3)
Ba = Button(fm_2,text='+',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_plus_clk)
Ba.grid(row=3,column=3)
Bm = Button(fm_2,text='-',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=btn_minus_clk)
Bm.grid(row=2,column=3)

Bce = Button(fm_2,text='^',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=sq)
Bce.grid(row=1,column=0)
Bc = Button(fm_2,text='C',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=C_clk)
Bc.grid(row=1,column=1)
Bsr = Button(fm_2,text='Sqrt',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=sqrt)
Bsr.grid(row=1,column=2)
Bb = Button(fm_2,text='<=',width=4,height=3,font=('Helvetica',10,'bold'),bd=10,command=back)
Bb.grid(row=1,column=3)


root.mainloop()
