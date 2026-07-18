# print a  right triangle
"""
*
**
***
****
*****
"""
n=5
num = n
for i in range(1,num+1):
    for j in range(i):
        print("*",end="")
    print()


