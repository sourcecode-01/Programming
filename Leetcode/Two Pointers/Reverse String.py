# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

s = ["h","e","l","l","o"]

l, r = 0, len(s) - 1
while l < r:
    s[l] , s[r] = s[r], s[l]
    l += 1
    r -= 1

print(s)