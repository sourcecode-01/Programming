class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set(nums)
        li = []
        
        for i in range(1,len(nums)+1):
            if i not in a:
                li.append(i)
        return li
