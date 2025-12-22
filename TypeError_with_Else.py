a = 24
b = "26"
try:
    res = a/b
except TypeError:
    print("Check your data type")
else:
    print(res)