# Input:
# nums = [3,4,5,6], target = 7
# Output: [0,1]

nums = [3,4,5,6]
target = 7

hash= {}

for indx, num in enumerate(nums):
    diff = target - num
    if diff in hash:
        print([hash[diff], indx])
    hash[num] = indx

