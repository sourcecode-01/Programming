class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        sum = 0
        for i in range(n):
            sum += nums[i]
         
        sum += target
        sum = sum // 2
        t = [[0 for i in range(sum + 1)]
            for i in range(n + 1)]
        for j in range(sum + 1):
            t[0][j] = 0
        for i in range(n + 1):
            t[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if (nums[i - 1] > j):
                    t[i][j] = t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j] + t[i - 1][j - nums[i - 1]]
        return t[n][sum]
