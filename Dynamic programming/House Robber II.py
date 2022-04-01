class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        def robber(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = nums[1]
            
            for i in range(2,len(nums)):
                dp[i] = max(nums[i-1],nums[i]+nums[i-2])
                
            return max(dp[-1],dp[-2])
        
        return max(robber(nums[1:]),robber(nums[:-1]))
