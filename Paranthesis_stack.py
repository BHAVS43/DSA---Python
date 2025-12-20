s = input()
stack = []
par = {')':'(', ']':'[', '}':'{'}
flag = True

for i in s:
    if i in "([{":
        stack.append(i)
    else:
        if not stack or stack[-1] != par[i]:
            flag = False
            break
        stack.pop()

if flag and not stack:
    print("valid")
else:
    print("invalid")
