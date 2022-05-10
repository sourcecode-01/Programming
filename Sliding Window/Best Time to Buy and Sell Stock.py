class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0
        
        while right < len(prices):
            curProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                maxProfit = max(maxProfit,curProfit)
            else:
                left = right
            right += 1
            
        return maxProfit
