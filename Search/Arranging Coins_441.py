class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 0,n
        
        while l <= r:
            mid = (l+r) // 2
            coin = mid*(mid+1)/2
            
            if coin == n:
                return mid
            elif coin > n:
                r = mid - 1
            else:
                l = mid + 1
        return r
