"""
10 10 10 10 10 10 10 10 10 10
9 9 9 9 9 9 9 9 9
8 8 8 8 8 8 8 8
7 7 7 7 7 7 7
6 6 6 6 6 6
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1"""
r=int(input("Enter Number OF Rows : "))
for i in range(r,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
