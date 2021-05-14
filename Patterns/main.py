""" # # #
    # #
    #"""
rows=int(input("Enter the number of rows"))
def pattern3(rows):
    for i in range(rows,0,-1):
        print("# "*i,end=" ")
        print()
pattern3(rows)