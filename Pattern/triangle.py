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


# Inverted Right Triangle
'''                                 
*****
****
***
**
*
'''

n=5
num = n
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()