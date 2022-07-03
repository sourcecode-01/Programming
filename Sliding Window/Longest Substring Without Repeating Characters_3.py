class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_ = set()
        res = 0
        l = 0
        
        for r in range(len(s)):
            
            while s[r] in set_:
                set_.remove(s[l])
                l += 1
            set_.add(s[r])
            res = max(res, r-l+1)
        
        return res
