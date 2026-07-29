arr = [1,5,3,4,5,3,7,3,9,5,1,6,5]
target = 5
count = 0
for i in range(len(arr)):
    if arr[i]==target:
        count = count+1

print(count)