class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret, cur = [], []
        def backtrack(ind):
            if ind == len(nums):
                ret.append(cur[:])
                return
            cur.append(nums[ind])
            backtrack(ind + 1)
            cur.pop()
            temp = ind
            while (temp < len(nums)) and (nums[temp] == nums[ind]):
                temp += 1
            backtrack(temp)
        backtrack(0)
        return ret
