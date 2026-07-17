arr = [12, 1, 52, 34, 10, 82]

largest = arr[0]
second_largest = -1

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i
    elif i < largest and i > second_largest:
        second_largest = i

print(second_largest)
