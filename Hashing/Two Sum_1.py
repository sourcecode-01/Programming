class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prearr = {}
        
        for i,n in enumerate(nums):
            diff = target-n
            if diff in prearr:
                return [prearr[diff],i]
            prearr[n]=i
        return
