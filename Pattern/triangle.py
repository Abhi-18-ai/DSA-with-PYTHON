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



# Right-Aligned Triangle
n = 5
num = n
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()


# Pyramid
''' 
    *
   ***
  *****
 *******
*********
'''
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()

# Inverted Pyramid
'''
*********
 *******
  *****
   ***
    *
'''
n= 5
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(2*(n-i)-1):
            print("*",end="")
    print()

# Diamond Pattern
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
n = 5
# Upper pyramid
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()


# Lower pyramid
for i in range(1, n):
    for j in range(i):
        print(" ", end="")
    for j in range(2 * (n - i) - 1):
        print("*", end="")
    print()