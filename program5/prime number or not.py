# To check the given number is prime or not
x=int(input("Enter the number"))
if x<=1:
    print("not prime")
else:
    for i in range(2,int(x/2)):
        if x%i==0:
            print("not prime number")
            break
    else:
       print("prime number")

