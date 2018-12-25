"""
Pattern-23:
     *
    * *
   * * *
  * * * *
 * * * * *
"""

r= int(input("Enter Rows : "))

for i in range(1,r+1):
    for j in range(r,i,-1):
        print("",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
