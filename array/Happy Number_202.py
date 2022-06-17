class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sqr(n)
            
            if n == 1:
                return True
        return False
        
    def sqr(self, n: int) -> int:
        output = 0
        
        while n:
            rem = n % 10
            rem = rem ** 2
            output += rem
            n = n // 10
        return output
