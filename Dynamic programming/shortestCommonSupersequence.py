class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        
        L = [[None] * (n+1) for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif str1[i-1] == str2[j-1]:
                    L[i][j] = L[i-1][j-1] + 1
                else:
                    L[i][j] = max(L[i-1][j],L[i][j-1])
                    
        li = []
        i = m
        j = n
        
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                li.append(str1[i-1])
                i-=1
                j-=1
            elif L[i-1][j] > L[i][j-1]:
                li.append(str1[i-1])
                i-=1
            else:
                li.append(str2[j-1])
                j-=1
                
        while i > 0:
            li.append(str1[i-1])
            i-=1
            
        while j > 0:
            li.append(str2[j-1])
            j-=1
            
        return "".join(li[::-1]) 
