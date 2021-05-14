#Sorting Array in Ascending array
from array import *
num=int(input("Enter the array length"))
val=array('i',[])
for i in range (num):
    ele=int(input("enter the next array element"))
    val.append(ele)
print(val)
def sort(val):
    for i in range(len(val)):
        for j in range((i+1),len(val)):

            if val[i]>val[j]:
                val[i],val[j]=val[j],val[i]
    print(val)
sort(val)




