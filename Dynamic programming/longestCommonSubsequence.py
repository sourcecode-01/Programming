class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        L = [[None] * (n+1) for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    L[i][j] = L[i-1][j-1] + 1
                else:
                    L[i][j] = max(L[i-1][j],L[i][j-1])
                    
        return L[m][n]
------------------------------------------------------------Printing LCS------------------------------------------------------------
    
 def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        L = [[None] * (n+1) for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    L[i][j] = L[i-1][j-1] + 1
                else:
                    L[i][j] = max(L[i-1][j],L[i][j-1])
                    
        li = []
        i = m
        j = n
        
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                li.append(text1[i-1])
                i-=1
                j-=1
            elif L[i-1][j] > L[i][j-1]:
                i-=1
            else:
                j-=1
                
        return "".join(li[::-1])
