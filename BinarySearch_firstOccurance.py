arr = [-1, 0, 17, 21, 23, 42, 42, 44, 48, 49]
target = 42
low = 0
high = len(arr)-1
indx = -1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        indx = mid
        low = mid + 1
        
    elif arr[mid] < target:
        low = mid + 1
    elif arr[mid] > target:
        high = mid - 1
print(indx)
        
