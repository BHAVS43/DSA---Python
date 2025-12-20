arr= [ 12, 12, 34 ]
for i in range(len(arr)):
    if i < 1:
        print("Array Index Out of Box")
    else:
        if arr[0] > arr[1]: 
            f_max = arr[0]
            s_max = arr[1]
        else: 
            f_max = arr[1]
            s_max = arr[0]

        for i in range(2, len(arr)):
            if arr[i] > f_max:
                s_max = f_max      
                f_max = arr[i]     
            elif arr[i] > s_max and arr[i] != f_max:
                s_max = arr[i]

print(s_max)
