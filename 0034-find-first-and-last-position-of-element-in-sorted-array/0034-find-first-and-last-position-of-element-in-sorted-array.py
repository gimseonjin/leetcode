"""
input - nums array, target
output - start and end target index in nums array

I should return it in log n

So I will use binary search!! 

first make binary search

and find the target's index!


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1,-1]
        
        if len(nums) == 1: 
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
    
        result = []
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = int((left + right) / 2 + 0.5)
            
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                start = mid
                end = mid
                
                while start > -1 and nums[start] == target :
                    start -= 1
                
                while end < len(nums) and nums[end] == target :
                    end += 1
                    
                result.append(start+1)
                result.append(end-1)
                break
        
        return result if result else [-1, -1]

"""

class Solution:
    
    def __init__(self):
        self.start = 0
        self.end = 0
        self.is_find = False
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1,-1]
        
        if len(nums) == 1: 
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        
        self.start, self.end = len(nums), -1
        
        def trees (n: list[int], target: int, mid: int):
            if len(n) == 1:
                if n[0] == target:
                    self.start = min(self.start, mid)
                    self.end = max(self.end, mid)
                    self.is_find = True
                return
            
            m = int(len(n) / 2 + 0.5)
            
            trees(n[:m], target, mid)
            trees(n[m:], target, mid+m)
        
        trees(nums, target, 0)
        
        return [self.start, self.end] if self.is_find else [-1,-1]
                
        