'''
이 문제는 아주 간단하게 O(n^2)로 풀 수 있을 거 같다
i 와 j를 전부 순회하면 풀 수 있을 것으로 예상된다.
다만 걱정인 것은 time lenght가 6 * 10^4 이여서 O(n^2)로 풀면 타임 아웃이 날 거 같다.

역시 났다!

아이디어가 생각이 안났는데 힌트를 보니 
We can count the number of songs having same (length % 60), and store that in an array of size 60.
라고 한다

즉 우리는 60으로 나눠지는지만 보면 된다.
나머지를 계산하고, 그 개수를 카운팅하면 된다.

예를 들어 [30,20,150,100,40] 인 경우

나머지, 30, 20, 30, 40, 40이고,

30 2개,
20 1개,
40 2개,


따라서 우선 길이 60짜리 하나 만들고 나머지 개수를 카운팅하자!

그리고 나머지가 0인 원소들끼리는 서로 합하면 0+0=0, 즉 60의 배수가 된다.
개수가 n개라면 가능한 쌍의 수는 n×(n-1)/2

나머지가 30인 경우 30+30=60이므로, 같은 방식으로 쌍을 만들 수 있다.
개수가 n개라면 n×(n-1)/2.

나머지가 0, 30이 아닌 경우
나머지가 i인 원소와 나머지가 60-i인 원소의 합은 항상 60의 배수가 된다.
예를 들어 나머지가 20인 개수가 1개이고, 나머지가 40인 개수가 2개이면,
가능한 쌍의 수는 1 × 2 = 2 쌍이다.

이러면 맨 처음 60의 나머지를 구하는 for문 O(N),
구한 60개의 나머지 리스트를 순회하는 경우, 이때 반만 도니까 O(30)

총 O(N)의 시간복잡도를 갖는다
'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_list = [0 for _ in range(60)]

        for t in time:
            remainder = t % 60
            remainder_list[remainder] += 1

        # 쌍의 수를 저장할 변수
        result = 0

        # 1. 나머지가 0인 경우: n개 중 2개를 선택하는 조합
        result += (remainder_list[0] * (remainder_list[0] - 1)) // 2

        # 2. 나머지가 30인 경우: n개 중 2개를 선택하는 조합
        result += (remainder_list[30] * (remainder_list[30] - 1)) // 2

        # 3. 나머지가 0과 30이 아닌 경우: 1 <= i < 30 인 경우, i와 60-i를 짝지음
        for i in range(1, 30):
            result += remainder_list[i] * remainder_list[60 - i]

        return result
        