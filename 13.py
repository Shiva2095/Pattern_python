"""Pattern-13:
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G
A B C D E F G H
A B C D E F G H I
A B C D E F G H I J"""

r=int(input("Enter Number OF Rows : "))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
    
