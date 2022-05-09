class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w1 = {x:0 for x in range(26)}
        w2 = {x:0 for x in range(26)}
        
        if len(s2) < len(s1):
            return False
        
        for i in range(len(s1)):
            w1[ord(s1[i]) - ord('a')] += 1
            w2[ord(s2[i]) - ord('a')] += 1
        
        start, end = 0, len(s1) - 1
        
        while end < len(s2):
            if w1 == w2:
                return True
            
            w2[ord(s2[start]) - ord('a')] -= 1
            start += 1
            end += 1
            
            if end < len(s2):
                w2[ord(s2[end]) - ord('a')] += 1
            
        return False
