"""
Pattern-16:
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1"""
r=int(input("Enter Number OF Rows : "))
for i in range(r,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
