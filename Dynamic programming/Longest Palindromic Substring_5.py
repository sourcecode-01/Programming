class Solution:
    def longestPalindrome(self, s: str) -> str:
        rev = s[::1]
        m = len(s)
        n = len(rev)
        res = 0
        
        L = [[None]* (n+1) for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif s[i-1] == rev[j-1]:
                    L[i][j] = L[i-1][j-1] + 1
                    res = max(res,L[i][j])
                else:
                    L[i][j] = 0
                    
        return res
