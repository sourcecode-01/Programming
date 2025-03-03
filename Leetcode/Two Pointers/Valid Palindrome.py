# Input: s = "Was it a car or a cat I saw?"
# Output: true

s = "Was it a car or a cat I saw?"
newStr = ""

for char in s:
    if char.isalnum():
        newStr += char.lower()

if newStr == newStr[::-1]:
    print("True")
