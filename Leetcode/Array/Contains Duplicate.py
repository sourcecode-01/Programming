# Input: nums = [1, 2, 3, 3]
# Output: true

nums = [1, 2, 3, 3]
seen = set()

for i in nums:
    if i in seen:
        print("True")
    else:
        seen.add(i)