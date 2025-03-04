# Input: s = "([{}])"
# Output: true

s = "([{}])"

stack = []
charToOpen = {")":"(", "}":"{", "]":"["}

for i in s:
    if i in charToOpen:
        if stack and stack[-1] == charToOpen[i]:
            stack.pop()
        else:
            print("False")
    else:
        stack.append(i)

if not stack:
    print("True")
else:
    print("False")
