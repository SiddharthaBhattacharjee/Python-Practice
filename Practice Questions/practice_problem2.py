list=[12,15,32,42,55,75,122,132,150,180,200]
list_2=[]
for x in list:
    if x<=150:
        if x%5==0:
            list_2.append(x)
        else:
            continue
    else:
        break
print(f'List before operation is {list}')
print(f'List after operation is {list_2}')
