class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openE,CloseE,s):
            if len(s) == 2*n:
                res.append(s)
                return
            if openE < n:
                backtrack(openE + 1,CloseE,s + "(")
            if CloseE < openE:
                backtrack(openE,CloseE + 1,s + ")")
        
        backtrack(0,0,"")
        return res
