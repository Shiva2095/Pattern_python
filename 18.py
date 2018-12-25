"""
Pattern-18:
A B C D E F G H I J
A B C D E F G H I
A B C D E F G H
A B C D E F G
A B C D E F
A B C D E
A B C D
A B C
A B
A
"""
r=int(input("Enter Number OF Rows : "))

for i in range(r,0,-1):
    for j in range(1,i):
        print(chr(64+j),end=" ")
    print()
    
