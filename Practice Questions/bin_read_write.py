L = [1001,1002,1003,1004,1005]

F = open(".//datao.bin" , 'wb')

for I in L:
    I=str(I)
    D = (I+'\n').encode()
    F.write(D)

F.close()

F = open(".//datao.bin" , 'rb')

L2=[]

for i in F:
    x=i.decode()
    x=x[:-1]
    x=int(x)
    print(x)

F.close()
