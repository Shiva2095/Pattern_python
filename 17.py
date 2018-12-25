"""Pattern-17:
A A A A A A A A A A
B B B B B B B B B
C C C C C C C C
D D D D D D D
E E E E E E
F F F F F
G G G G
H H H
I I
J
"""
r=int(input("Enter Number OF Rows : "))

for i in range(1,r+1):
    for j in range(i,r+1):
        print(chr(64+i),end=" ")
    print()
    
