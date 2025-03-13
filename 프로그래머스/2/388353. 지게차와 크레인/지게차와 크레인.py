"""
컨테이너가 m * n 개가 있다.

지게차로 접근 가능한 종류의 모든 컨테이너를 가져온다.

1면이 외부와 연결되어 있으면 된다.

크레인을 사용하면 연결되어 있지 않아도 꺼낼 수 있다.

A 하나면 지게차, BB 처럼 두 개 연달아는 크레인

아 크레인으로 하면 그냥 다 제거하면 되는데
지게차로 할 경우, 상하좌우로 이동했을 때, 끝에 닿을 수 있냐 없냐가 핵심이네
"""
from collections import deque

def use_crane(request: str) -> bool:
    return len(request) == 2  # 크레인은 두 개 연속된 문자일 때 사용

def can_move(storage, x, y, n, m):
    queue = deque([(x, y)])
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 이동 정의
    visited = set()
    
    while queue:
        i, j = queue.popleft()
        
        # 외부에 닿을 수 있는지 확인
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            return True  

        for dx, dy in DIRECTIONS:
            ni, nj = i + dx, j + dy

            # 이미 방문한 위치는 스킵
            if (ni, nj) in visited:
                continue

            if 0 <= ni < n and 0 <= nj < m and storage[ni][nj] == "0":  
                queue.append((ni, nj))
                visited.add((ni, nj))

    return False  # 끝까지 탐색했지만 경계에 닿지 않음

def take_container_from(storage, request, n, m):
    temp = []
    visited = set()  # 같은 요청 내에서 중복 검사 방지

    for i in range(n):
        for j in range(m):
            if storage[i][j] == request[0]:  # 컨테이너 발견
                if use_crane(request):  
                    temp.append((i, j))  # 크레인은 무조건 제거
                elif (i, j) not in visited and can_move(storage, i, j, n, m):
                    temp.append((i, j))  # 지게차로 이동 가능하면 제거 대상 추가

    # 컨테이너 제거
    for x, y in temp:
        storage[x][y] = "0"
    
    return len(temp)

def solution(storage, requests):
    storage_list = [list(row) for row in storage]  # 문자열을 2차원 리스트로 변환
    n = len(storage_list)
    m = len(storage_list[0])
    result = n * m  # 전체 컨테이너 개수

    for request in requests:
        result -= take_container_from(storage_list, request, n, m)
        
    return result
