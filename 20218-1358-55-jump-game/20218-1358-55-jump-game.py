"""
즉, 모든 인덱스를 뛰어가면서, 마지막 인덱스에 도착할 수 있냐!! 라는 검증 로직이다.

그냥 dfs로 쭈욱 계산해나가면 풀리는데, 이미 계산한 부분을 또 하기 때문에 타임 오버가 뜬다

따라서 계산 결과값 일부는 저장해서 그걸 재활용하는 식으로 풀면 될 듯 하다
"""
class Solution:
    def __init__(self):
        self.cache = {}  # 각 인덱스에 대해 도달 가능 여부를 저장하는 내부 변수

    def _dfs(self, nums: List[int], index: int) -> bool:
        # 이미 계산된 인덱스라면 결과 반환
        if index in self.cache:
            return self.cache[index]

        # 마지막 인덱스 또는 그 이후에 도달한 경우 성공
        if index >= len(nums) - 1:
            return True
        
        furthest = min(index + nums[index], len(nums) - 1)
        for next_index in range(index + 1, furthest + 1):
            if self._dfs(nums, next_index):
                self.cache[index] = True
                return True

        self.cache[index] = False  # 이 인덱스에서는 마지막 인덱스에 도달 불가능
        return False

    def canJump(self, nums: List[int]) -> bool:
        self.cache = {}  # 캐시 초기화
        return self._dfs(nums, 0)
