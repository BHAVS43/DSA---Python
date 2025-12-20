arr = [1, 2, 15, 65,  12, 95, 76]
flag = False
indx = -1
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        
        if arr[i] == arr[j]:
            flag = True
            indx = i
if flag:
    print("This is a bad array")
else:
    print("This is a good array")
        
        
        
