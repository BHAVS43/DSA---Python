arr = [12, 45, 73, 90, -2, 35, 12, 45, 90, -2]
arr.sort()
print(arr)

frequency = {}

for i in range(len(arr)):
    if arr[i] not in frequency:
        frequency[arr[i]] = 1
    elif arr[i] in frequency:
        frequency[arr[i]]+=1
        
        
print(frequency)
    

