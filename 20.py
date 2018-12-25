"""
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2
10 9 8 7 6 5 4 3
10 9 8 7 6 5 4
10 9 8 7 6 5
10 9 8 7 6
10 9 8 7
10 9 8
10 9
10"""

r=int(input("Enter Number OF Rows : "))
for i in range(1,r+1):
    for j in range(r,i-1,-1):
        print(j,end=" ")
    print()
    
