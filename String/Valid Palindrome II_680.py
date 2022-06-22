class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        
        while l < r:
            if s[l] != s[r]:
                lside , rside = s[l+1:r+1], s[l:r]
                return (lside == lside[::-1] or rside == rside[::-1])
            l,r = l+1, r-1
        return True
