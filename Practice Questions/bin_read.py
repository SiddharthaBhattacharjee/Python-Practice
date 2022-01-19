L=[]

F = open(".//data.bin",'rb')


for i in F:
    j = i.decode()
    L.append(j)

print(L)
F.close()
