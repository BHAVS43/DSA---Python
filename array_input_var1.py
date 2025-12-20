arr = list(map(int,  input().split()))
k = int(input("Enter a number: "))
found = False
indx = -1
for i in range(len(arr)):
    if k == arr[i]:
        flag = True
        indx = i+2
if found:
    print("k found at index", indx)
else:
    print(indx)
    
    
