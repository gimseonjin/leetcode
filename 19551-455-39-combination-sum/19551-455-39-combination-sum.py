"""
전형적인 조합 문제로 dfs & 백트래킹으로 풀 수 있다

python의 combination 함수 좋은 게 많지만 이번에는 안쓰고 풀어봅시다!

재귀로 가볍게 만들어봅시다 최대 조합의 길이는 150이라니까 재귀로 해도 큰 문제 없을 듯?
"""

class Solution:
    def dfs(self, candidates, current, depth, target, result):
        # 종료 조건: 깊이 제한 또는 현재 합이 target보다 커지면 중단
        if sum(current) > target or depth == 150:
            return

        if sum(current) == target:
            result.add(tuple(sorted(current.copy())))
            return

        for candidate in candidates:
            current.append(candidate)
            self.dfs(candidates, current, depth + 1, target, result)
            current.pop()  # 마지막 추가한 요소 제거

    def combinationSum(self, candidates, target):
        result = set()
        self.dfs(candidates, [], 0, target, result)
        return list(result)