# Find 3rd Largest number in an array

def third(array):
    n = len(array)
    largest = float("-inf")
    s_largest = float("-inf")
    # third_largest = array[0]
    for i in range(0,n):
        if array[i]>largest:
            # third_largest=s_largest
            s_largest=largest
            
            largest=array[i]
        elif array[i]>s_largest and array[i]!=largest:
            s_largest=array[i]
        # elif array[i]>third_largest and array[i]!=s_largest:
        #     third_largest=array[i]
            return s_largest
array = [4,56,79,997,10]
result = third(array)
print(result)
