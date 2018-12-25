"""Pattern-5:
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J"""

r=int(input("Enter Number Of Rows : "))
c=int(input("Enter Number Of Column : "))

for i in range(1,r+1):
    for j in range(1,c+1):
        print(chr(64+j),end=" ")
    print()
    
