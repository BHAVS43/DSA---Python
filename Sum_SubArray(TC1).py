arr = [-15,-20,-1,-3]
maxi = arr[0]
for i in range(len(arr)):
    count = 0
    for j in range(i, len(arr)):
        count = count + arr[j]
        if maxi < count:
            maxi = count
print(maxi)
