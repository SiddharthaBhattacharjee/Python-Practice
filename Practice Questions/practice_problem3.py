list=[10,20,30,40,50,60,70,80,90,100]
for i in range(0,len(list)-1,2):
    x = list[i]
    a=i
    print(f"position : {a} , Element : {x}")

print('\n')
# or

for a,x in (enumerate(list)):
    if a%2==0:
        print(f"Position : {a} , Element : {x}")

    
