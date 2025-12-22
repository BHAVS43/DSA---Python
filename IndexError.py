arr = [1,2,3,4,5]
print(arr[4])
try:
    print(arr[5])
except IndexError:
    print("Check the range of your array")