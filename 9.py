"""Pattern-9:
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
"""

r=int(input("Enter Number OF Rows : "))
#code 1
"""for i in range(0,r):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
"""
for i in range(0,r):
    print("* "*(i+1))
