def merge(arr, low, mid, high):
    p1 = low
    p2 = mid + 1
    new_arr = []
    
    while p1 <= mid and p2 <= high:
        if arr[p1] <= arr[p2]:
            new_arr.append(arr[p1])
            p1 = p1 + 1
        else:
            new_arr.append(arr[p2])
            p2 = p2 + 1
            
    while p1 <= mid:
        new_arr.append(arr[p1])
        p1 = p1 + 1
        
    while p2 <= high:
        new_arr.append(arr[p2])
        p2 = p2 + 1
        
    indx = low
    for i in range(len(new_arr)):
        arr[indx] = new_arr[i]
        indx = indx + 1   

def divide(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
           
    divide(arr, low, mid)
    divide(arr, mid+1, high)
    merge(arr, low, mid, high)

arr = [2, 53, -13, 57, 64, -80]
print(arr)
    
divide(arr, 0, len(arr)-1)
print(arr)  

