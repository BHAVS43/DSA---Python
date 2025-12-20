arr = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]]
sum1 = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        
        sum1 = sum1 + arr[i][j]
        
print(sum1)
