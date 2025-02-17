"""
logs는 id와 minute을 페어로 가진 리스트다.

거기서 id로 unique한 minute을 카운팅하는 로직이다.

우선 제일 간단한 로직은 map을 만들고, key는 id, value는 minute를 담는 Set 자료형이 된다.
모든 logs를 순회하면서 map에 적재를 하고, 모든 순환 후, 각 value의 size를 계산 후 배열에 담으면 된다.

시간 복잡도를 계산해보면, 우선 logs를 순회해야하니 O(10^4)가 될 것이고,
순환한 결과의 key를 한번 더 돌면서, size를 계산해서 List에 +1하면 O(10^4)가 될 것이다

O(10^4 + 10^4) 해서 O(2 * 10^4)이 될 것이다.
"""
from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # 각 유저(user_id)가 활동한 분(minute)을 저장하는 딕셔너리
        user_minutes = defaultdict(set)
        for user_id, minute in logs:
            user_minutes[user_id].add(minute)

        # 각 유저의 UAM(활동 분 수)를 계산
        # 결과 배열은 0-indexed로, answer[j]는 UAM이 j+1인 유저의 수를 의미
        result = [0 for _ in range(k)]
        for minutes in user_minutes.values():
            uam = len(minutes)
            result[uam - 1] += 1
        
        return result
        