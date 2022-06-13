class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            for i in range(1,len(nums)):
                if i == 1:
                    maxnum = nums[i]
                else:
                    maxnum = nums[i-2] + nums[i]
                    
                nums[i] = max(maxnum, nums[i-1])
                
        return max(nums[len(nums) - 2],nums[len(nums) - 1])
