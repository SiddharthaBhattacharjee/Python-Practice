def isprime(x):
    if x==1:
        print("NPNC")
    else:
        prime_flag = 0
        i=2
        while(i*i<=x):
            if x%i==0:
                prime_flag = 1
                break
            else:
                i += 1
        if prime_flag:
            return "Composit"
        elif not prime_flag:
            return "Prime"
if __name__ == "__main__":
    while True:
        x=int(input("Enter a number : "))
        print("The entered no is : ",isprime(x))
        
