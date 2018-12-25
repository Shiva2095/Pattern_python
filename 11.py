"""Pattern-11:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8"""
r=int(input("Enter Number OF Rows : "))

for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
