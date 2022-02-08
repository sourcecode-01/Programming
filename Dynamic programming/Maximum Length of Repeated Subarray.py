class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        res = 0
        
        L = [[None] * (n+1) for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif nums1[i-1] == nums2[j-1]:
                    L[i][j] = L[i-1][j-1] + 1
                    res = max(res, L[i][j])
                    
                else:
                    L[i][j] = 0
                    
        return res
