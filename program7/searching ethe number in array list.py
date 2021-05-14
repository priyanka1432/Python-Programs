from array import *
val=array('i',[])
x=int(input("Enter the array length"))
for i in range(x):
    y=int(input("Enter the next element"))
    val.append(y)
print(val)
val.reverse()
print(val)
k=0
num=int(input("Enter the number to be searched"))
for e in val:
    if e==num:
        print(k)
        break
    k+=1
else:
    print("number is not found")