# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

nums = [1,2,2,3,3,3,3]
k = 2

count = {}
for i in nums:
    count[i] = 1 + count.get(i, 0)

arr = []
for key, value in count.items():
    arr.append([value, key])

arr.sort()
res = []

while len(res) < k:
    res.append(arr.pop()[1])

print(res)