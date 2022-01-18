alist = [12,34,13,45,22,19,88,10,65,56,99,20]
alist.sort()
array = alist
def search(array,x):
    f = 0
    l = len(array)-1
    while l>=f:
        mid = int((f+l)/2)
        if array[mid]==x:
            return mid
        
        elif array[mid]>x:
            l = mid-1
        elif array[mid]<x:
            f = mid+1

if __name__ == "__main__":
    print(array)
    while True:
        x = int(input("Enter no to be searched : "))
        print("Position in aray is : ",search(array,x))
        print()
            
        
        
