class Solution:
    def get_index(self, nums: List[int], target: int, getfirst: bool):
            s = 0
            e = len(nums) - 1
            ans = -1
        
            while(s<=e):
                mid = ( s + e ) // 2
                if (nums[mid] == target):
                    ans = mid
                    if(getfirst):   
                        e = mid -1
                    else:
                        s = mid + 1
                elif (nums[mid]>target):
                    e = mid -1
                else:
                    s = mid + 1
            return ans
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.get_index(nums,target,True)
        last = self.get_index(nums,target,False)
        output = [first,last]
        return output
        
