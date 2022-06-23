class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a = Counter(text)
        b = Counter("balloon")
        
        res = len(text)
        for i in b:
            res = min(res, a[i] // b[i])
        return res
