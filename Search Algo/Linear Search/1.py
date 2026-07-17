# Given an array and a target value, check element exist or Not.

arr =[1,2,5,6,8]

def linear(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return target
    return -1

result = linear(arr,6)

if result != -1:
    print(result,"it exist")
else:
    print("not found")