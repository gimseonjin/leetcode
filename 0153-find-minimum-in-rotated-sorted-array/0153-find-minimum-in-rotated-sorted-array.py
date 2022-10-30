class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        def dfs(nums,target):
            if len(nums) == 1:
                return min(target, nums[0])
            
            mid = int(len(nums) / 2 + 0.5)
            
            return min(dfs(nums[:mid],target), dfs(nums[mid:],target))
        
        return dfs(nums,5001)