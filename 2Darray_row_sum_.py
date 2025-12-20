arr = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]]
sum1 = 0
for i  in range(len(arr)):
    for j in range(len(arr[i])):
        if i+j == len(arr)-1:
            sum1 = sum1 + arr[i][j]
print(sum1)
