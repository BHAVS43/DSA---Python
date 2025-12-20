int1 = 125
string = str(int1)
newString = string[::-1]
print(newString)
if string == newString:
    print("int1 is palindrome")
else:
    print("int1 is not palindrome")
