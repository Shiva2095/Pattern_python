"""
Pattern-7:
J J J J J J J J J J
I I I I I I I I I I
H H H H H H H H H H
G G G G G G G G G G
F F F F F F F F F F
E E E E E E E E E E
D D D D D D D D D D
C C C C C C C C C C
B B B B B B B B B B
A A A A A A A A A A"""

r=int(input("Enter No. Of Row : "))
c=int(input("Enter Number Of Column : "))

for i in range(r,0,-1):
    for j in range(c,0,-1):
        print(chr(64+i),end=" ")
    print()
    
