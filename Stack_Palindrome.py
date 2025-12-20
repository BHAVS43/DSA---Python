s = input()

stack = []
rev = ""
for i in s:
    stack.append(str(i))
    
    while stack:
        rev = rev + stack[-1]
        stack.pop()
if s == rev:
    print("Not Palindrome")
else:
    print("Palindrome")
