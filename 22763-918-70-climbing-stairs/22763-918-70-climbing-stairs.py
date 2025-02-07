'''
이건 모든 조합을 구하는 거다
dfs를 쓰면 되겠지
depth만큼 타고 들어가면서 모든 조합을 만들면 될 듯!

이라고 했지만 재귀 형태로 하니까 시간 복잡도가 높아서 타임 리밋에 걸림

와우 인터넷 찾아보니 이건 피보나치 수열 푸는 것처럼 풀 수 있다네

마지막 한 칸이 남는 경우는 n-1 개의 계단을 걷는거고 그 경우의 수는 f(n-1)
마지막 두 칸이 남는 경우는 n-2 개의 계단을 걷는거고 그 경우의 수는 f(n-2)
'''

class Solution:
    # 이 부분은 타임아웃 걸리긴 했지만 dfs 사용한 케이스'
    def dfs(self, stepSums: int, targetStep: int):
        # 목표 계단에 도달한 경우
        if stepSums == targetStep:
            self.count += 1
            return
        # 목표를 초과한 경우
        if stepSums > targetStep:
            return

        # 한 계단 오르는 경우와 두 계단 오르는 경우 재귀 호출
        self.dfs(stepSums + 1, targetStep)
        self.dfs(stepSums + 2, targetStep)

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        a, b = 1, 1  # a: f(n-2), b: f(n-1)
        for _ in range(2, n + 1):
            a, b = b, a + b  # f(n) = f(n-1) + f(n-2)
        
        return b
