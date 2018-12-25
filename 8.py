"""Pattern-8:
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A"""
r=int(input("Enter Number Of Row : "))
c=int(input("Enter Number Of Column : "))

for i in range(r,0,-1):
    for j in range(c,0,-1):
        print(chr(64+j),end=" ")
    print()
