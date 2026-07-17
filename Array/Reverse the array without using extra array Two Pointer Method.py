arr=[12,4,25,99,85,65,10,15,2,8,34]

start = 0  #starting index
end = len(arr)-1  #last index

while start<end:     # swaping is possible until it is true
    arr[start],arr[end] = arr[end],arr[start] #swaping
    start+=1
    end-=1
    
print(arr)