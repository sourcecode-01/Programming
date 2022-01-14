def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxSum = nums[0]
        for i in range(1,len(nums)):
            currSum += nums[i]
            currSum = max(currSum, nums[i])
            maxSum  = max(maxSum, currSum)
            
        return maxSum
