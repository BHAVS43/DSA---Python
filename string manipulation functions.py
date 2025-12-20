#String manipulation functions
name = input("Enter your name: ")          #taking input from user

string1 = "Bhavana"
string2 = "Medi"

length = len(string1)             #length of string
print(length)

print(string1[0:7])
print(string2[:4])               #slicing
print(string1[0])                #indexing
print(string2[::-1])
print(string1[-1:3])

print(string1 + " " + string2)          #string concatination

print(name * 2)                   #string repetition

print(string1.upper())          #converting to uppercase letters

print(string2.lower())          #converting to lowercase letters

print(name.swapcase())          #converting to Uppercase to Lowercase and viceversa



