# Input: s = "racecar", t = "carrace"
# Output: true

s = "racecar"
t = "carrace"

if len(s) != len(t):
    print("False")

maps, mapt = {}, {}

for i in range(len(s)):
    maps[s[i]] = 1 + maps.get(s[i], 0)
    mapt[t[i]] = 1 + mapt.get(t[i], 0)

if maps == mapt:
    print("True")
