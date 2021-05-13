aval=20
x=int(input("enetr no."))
for i in range(1,x+1):
    if i>aval:
        print("U will got" ,aval,x-aval,"not there")
        print("out of stock")
        break
    print("hi",i)

