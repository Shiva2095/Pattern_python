"""Pattern-6:
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1"""

r=int(input("Enter Number Of Row : "))
c=int(input("Enter Number Of Column : "))
for i in range(r,0,-1):
    for j in range(c,0,-1):
        print(j,end=" ")
    print()
