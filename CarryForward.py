arr = [23,24,10,61,7,12,14,96]
c_arr = []
maxi = arr[0]
for i in range(len(arr)):
    if maxi < arr[i]:
        maxi = arr[i]
        c_arr.append(maxi)
    else:
        c_arr.append(maxi)
print(c_arr)
