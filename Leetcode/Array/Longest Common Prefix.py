# Input: strs = ["flower","flow","flight"]
# Output: "fl"

strs = ["flower","flow","flight"]
prifix = ""

for char in zip(*strs):
    if len(set(char)) == 1:
        prifix += char[0]

print(prifix)
