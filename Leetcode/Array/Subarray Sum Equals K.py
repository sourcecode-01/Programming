# Input: nums = [1,1,1], k = 2
# Output: 2

nums = [1,1,1]
k = 2

prefix_sum = { 0 : 1 }
currSum, res = 0, 0

for num in nums:
    currSum += num
    diff = currSum - k

    res += prefix_sum.get(diff, 0)
    prefix_sum[currSum] = 1 + prefix_sum.get(currSum, 0)

print(res)