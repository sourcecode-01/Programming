class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        res = []
        
        def search(i, string):
            if len(string) == len(digits):
                res.append(string)
                return
            
            chars = mapping[digits[i]]
            
            for char in chars:
                search(i + 1, string + char)
            
        if digits:
            search(0, "")
        
        return res
