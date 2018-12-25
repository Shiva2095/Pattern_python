"""
J J J J J J J J J J
I I I I I I I I I
H H H H H H H H
G G G G G G G
F F F F F F
E E E E E
D D D D
C C C
B B
A
"""
r= int(input("Enter Number Of Rows : "))
for i in range(r,0,-1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
    
