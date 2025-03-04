"""
A도둑 B도둑 팀
누구도 안잡히도록 

i 훔칠 때, A는 info[i][0] B는 info[i][1] 흔적, 1이상 3이하

A 도둑은 n개 이상, B 도둑은 m개 이상

이거 dfs로 쭈우욱 가면서 최솟 값을 넘기면 되겠다
"""
from functools import lru_cache

MAX_INTEGER = 121  # 최악의 경우보다 1 큰 값 (불가능한 경우를 표현)

def solution(info, n, m):
    @lru_cache(None)  # 메모이제이션 적용 (중복 탐색 방지)
    def dfs(depth, a_sum, b_sum):
        # 가지치기 1: 이미 A 도둑 흔적이 최소값 이상이면 탐색할 필요 없음
        if a_sum >= n:
            return MAX_INTEGER
        
        # 가지치기 2: B 도둑이 이미 경찰에게 잡히면 더 이상 탐색할 필요 없음
        if b_sum >= m:
            return MAX_INTEGER

        # 모든 물건을 처리한 경우
        if depth == len(info):
            return a_sum if a_sum < n and b_sum < m else MAX_INTEGER
        
        # 현재 물건을 A 도둑이 훔치는 경우
        next_a_info = dfs(depth + 1, a_sum + info[depth][0], b_sum)

        # 현재 물건을 B 도둑이 훔치는 경우
        next_b_info = dfs(depth + 1, a_sum, b_sum + info[depth][1])

        return min(next_a_info, next_b_info)  # 최소 흔적 선택
    
    answer = dfs(0, 0, 0)
    return -1 if answer == MAX_INTEGER else answer
