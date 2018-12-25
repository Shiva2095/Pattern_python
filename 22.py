"""
Pattern-22:
J I H G F E D C B A
J I H G F E D C B
J I H G F E D C
J I H G F E D
J I H G F E
J I H G F
J I H G
J I H
J I
J"""
r= int(input("Enter Number Of Rows : "))
for i in range(1,r+1):
    for j in range(r,i-1,-1):
        print(chr(64+j),end=" ")
    print()
    

