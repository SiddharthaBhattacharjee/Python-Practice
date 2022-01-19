L = ['Harry',"Sid","Krish",'Joy']

F = open(".//data.bin" , 'wb')

for I in L:
    D = (I+'\n').encode()
    F.write(D)

F.close()

F = open(".//data.bin" , 'rb')

L2=[]

for i in F:
    x=i.decode()
    x=x[:-1]
    print(x)

F.close()

