# Example 1:
#
# Input: nums = [3,2,3]
# Output: [3]

# Example 2:
#
# Input: nums = [1,2]
# Output: [1,2]

nums = [1,2]
counter = {}
result = []

for i in nums:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

for key in counter:
    if counter[key] > len(nums) // 3:
        result.append(key)

print(result)