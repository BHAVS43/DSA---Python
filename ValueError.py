try:
    a = int(input())
    b = int(input())
    res = a + b
except ValueError:
    print("Enter the correct value")
else:
    print(res)

