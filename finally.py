a = 24
b = "26"
try:
    res = a + b
except  TypeError:
    print("Check your Data Type")
else:
    print(res)
finally:
    print("End of Code")