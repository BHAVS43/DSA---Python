def prefix(arr, left, right):
    pre_arr = []
    sum = 0
    for i in arr:
        sum += i
        pre_arr.append(sum)

    print("Prefix Array is:", pre_arr)

    count = 0
    for i in range(left, right + 1):
        if arr[i] % 2 == 0:
            count += 1

    return count


arr = [10, 21, 30, 45, 50, 62]

left = int(input())
right = int(input())

result = prefix(arr, left, right)
print("Even numbers count =", result)
