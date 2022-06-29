class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
            
        for i in range(len(s)):
            
            temp = validString(i, i, s)
            if len(temp) > len(res):
                res = temp
            
            temp = validString(i, i + 1, s)
            if len(temp) > len(res):
                res = temp
                
        return res
            
    
def validString(left, right, s):
    left_p = left
    right_p = right

    while left_p >= 0 and right_p < len(s) and s[left_p] == s[right_p]:

        left_p -= 1
        right_p += 1
        
    return s[left_p+1:right_p] 
