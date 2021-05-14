"""
          *
         * *
        * * *
         * *
          *
"""
rows=int(input("Enter the number of rows"))
k=2*rows-2
def pattern4(rows):
    for i in range(1,rows+1):
        for j in range(1,k):
            print(end=" ")
            k-=2
        for j in range(0,i+1):
            print(" * ",end=" ")
            print("")
pattern4(rows)