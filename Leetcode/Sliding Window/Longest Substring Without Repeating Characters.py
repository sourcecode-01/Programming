# Input: s = "abcabcbb"
# Output: 3

s = "abcabcbb"

charSet = set()
l, res = 0, 0

for r in range(len(s)):
    while s[r] in charSet:
        charSet.remove(s[l])
        l += 1
    charSet.add(s[r])
    res = max(res, r - l + 1)

print(res)