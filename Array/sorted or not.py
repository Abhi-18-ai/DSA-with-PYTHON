# A given array , you have to return true if sorted or false if not sorted

def sorted(array):
    n = len(array)
    for i in range(0,n-1):
        if array[i]>array[i+1]:
            return False

    return True

array = [2,4,4,6,8,9,10]
result = sorted(array)
print(result)