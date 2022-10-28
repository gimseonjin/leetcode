class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = Solution.find_x(matrix, target)
        
        if x == -1:
            return False
        
        row = matrix[x]
        
        left, right = 0, len(row)-1
        
        while left <= right:
            mid = int((left+right)/2)
            
            if row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
        else:
            return False
            
    
    def find_x(matrix: List[List[int]], target: int):
        for i, m in enumerate(matrix):
            if m[len(m)-1] >= target:
                return i
        else:
            return -1