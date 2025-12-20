arr = [-1,2,-3,4]
mini = arr[0]
arr2 = []
for i in range(len(arr)):
    for j in range(i, len(arr)):
        count = 0
        for k in range(i, j+1):
            count = count + arr[k]
        if mini > count:
            mini = count
           
print(mini)

