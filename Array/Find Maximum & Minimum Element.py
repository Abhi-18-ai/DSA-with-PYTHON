arr=[12,4,25,99,85,65,10,15,2,8,34]


max = arr[0] # we assume that maximum value is at 0th index
min = arr[0] # we assume that minumum value is at 0th index
    
for i in (arr):
    if i>max:
        max=i
            
    if i<min:
        min=i
            
            
print(max,min)