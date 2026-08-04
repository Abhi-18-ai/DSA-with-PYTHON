

def selection_sort(array):
    n = len(array)
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if array[j]<array[min_index]:
                min_index = j

            array[j],array[min_index] = array[min_index],array[j]

answer = selection_sort([2,5,1,4,8,6,9,7])
print(answer)