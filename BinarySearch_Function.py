def Binary(arr, low, high, target):
    
    if low > high:
        return -1
        
    sumlh = low + high
    mid = int(sumlh/2)
    
    if arr[mid] == target:
        return mid
           
    elif arr[mid] < target:
        return Binary(arr, mid+1, high, target)    
    else:
        return Binary(arr, low, mid-1, target)
        
arr1 = [-1,0,17,17,17,21,23,42,44,44,49,53]
k = 44
l = 0
h = len(arr1)-1
print(Binary(arr1, l, h, k))
