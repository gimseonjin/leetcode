"""
이건 조합 문제다.
dfs를 사용하면 쉽게 풀릴 듯
"""
class Solution:
    def dfs(self, nums: List[int], subset: List[int], depth: int, result: List[List[int]]):
        # 모든 원소에 대해 선택 여부를 결정했다면 부분집합을 결과에 추가
        if depth == len(nums):
            result.append(subset.copy())
            return
        
        # 현재 원소를 포함하는 경우
        subset.append(nums[depth])
        self.dfs(nums, subset, depth + 1, result)

        # 백트래킹: 원소 제거
        subset.pop()  
        # 현재 원소를 포함하지 않는 경우
        self.dfs(nums, subset, depth + 1, result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        self.dfs(nums, subset, 0, result)
        return result
        