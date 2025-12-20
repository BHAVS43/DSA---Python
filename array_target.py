arr = [1, 12, 15, 65, 14, 95, 76]
target = 13
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        sum = arr[i] + arr[j]
        if sum == target:
            print(arr[i])
            print(arr[j])
               
    
