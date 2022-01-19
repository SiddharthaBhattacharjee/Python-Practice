list = [10,20,30,40,50,60]
#list_2=[]
print(f'The list before reverse is {list}')
"""
list = list[::-1]
print(f'List after reversing is {list}')
for i in range(0,len(list)-1,-1):
    list_2.append(i)
print(f'The list after reversing is {list_2}')"""

list.reverse()
print(f'The list after reversing is {list}')
