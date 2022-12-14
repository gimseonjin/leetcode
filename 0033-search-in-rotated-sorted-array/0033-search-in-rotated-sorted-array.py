class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_k(nums):
            k = 0
            
            if nums[0] < nums[len(nums)-1]:
                return k
            
            while k+1 < len(nums) and nums[k] < nums[k+1]:
                k += 1
                
            return k+1
        
        def rotation(nums, k):
            return nums[k:] + nums[:k]
        
        if len(nums) == 0:
            return -1
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        k = find_k(nums)
        result = rotation(nums, k)
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = int((left+right)/ 2 + 0.5)
            
            if result[mid] > target:
                right = mid-1
            elif result[mid] < target:
                left = mid+1
            else:
                return (mid + k) % len(nums)
        
        return -1