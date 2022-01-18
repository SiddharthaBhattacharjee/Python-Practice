"""
Statement : You are given a quadrilateral WXYZ ,
write a program that takes coordinates of w,x,y & z as input and determine the type of
quadrilateral , out of rombus, square , rectangle and parallelogram.
"""

'''

(a,b)W                X(c,d)
      .--------------.
      |                |
      |      .(p,q) |
      |                |
      |                |
      .--------------.
    Z(g,h)       (e,f)Y  

let mid pt of WZ be (k,l)
let mid pt of XY be (m,n)

let U=WZ and V=XY

let WY(length)=L and YZ(breadth)=B

 '''
while(True):
    print('''
    Let WXYZ be the Quadrilateral
    Enter the coordinate of W,X,Y,Z (X coordinate and Y coordinate separately)
    The algorithm will determine the special type of quadrilateral
    from : (Arbitrory, Square, Rectangle, Rhombus, Parallelogram)''')

    a=int(input('Enter X coordinate of W : '))
    b=int(input('Enter Y coordinate of W : '))
    c=int(input('Enter X coordinate of X : '))
    d=int(input('Enter Y coordinate of X : '))
    e=int(input('Enter X coordinate of Y : '))
    f=int(input('Enter Y coordinate of Y : '))
    g=int(input('Enter X coordinate of Z : '))
    h=int(input('Enter Y coordinate of Z : '))

    k=(a+e)/2
    l=(b+f)/2

    m=(c+g)/2
    n=(d+h)/2
    
    U=(  ((e-a)**(2)) + ((f-b)**(2)) )**(1/2)
    V=(  ((g-c)**(2)) + ((h-d)**(2)) )**(1/2)

    L=(  ((g-a)**(2)) + ((h-b)**(2)) )**(1/2)
    B=(  ((e-g)**(2)) + ((f-h)**(2)) )**(1/2)


    if k!=m or l!=n :
        print('The Given quadrilateral is Arbitrary')
    elif k==m and l==n :
        if U==V:
            if L==B:
                print('The given quadrilateral is a Square')
            else:
                print('The given quadrilateral is a Rectangle')
        elif U!=V :
            if L==B:
                print('The given quadrilateral is a Rhombus')
            else:
                print('The given quadrilateral is a paralelogram')
                
                
        

