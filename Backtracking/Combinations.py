class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(st,curr):
            if len(curr) == k:
                res.append(curr)                
            
            for i in range(st,n+1):
                dfs(i+1, curr+[i])
                
        dfs(1,[])
        return res
