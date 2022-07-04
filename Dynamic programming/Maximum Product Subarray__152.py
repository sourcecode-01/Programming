class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        _max = _min = nums[0]
        max_product = _max
        
        for i in range(1, len(nums)):
            curr_num = nums[i]
            
            temp_min = _min
            _min = min(curr_num, _max * curr_num, _min * curr_num)
            _max = max(curr_num, _max * curr_num, temp_min * curr_num)
            
            max_product = max(max_product, _max)
        
        return max_product
