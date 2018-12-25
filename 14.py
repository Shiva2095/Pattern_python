"""Pattern-14:
* * * * * * * * * *
* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*"""
#Input
r=int(input("Enter Number OF Rows : "))
#code 1
"""for i in range(0,r):
    print("*"*(r-i))
"""
# code 2
for i in range(r,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
    
