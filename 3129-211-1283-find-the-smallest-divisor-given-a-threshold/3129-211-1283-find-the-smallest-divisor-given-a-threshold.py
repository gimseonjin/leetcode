"""
이건 양의 정수로 나눴을 때, 몫을 전부 더해서 그 결과가 threshold보다 작은 최소 정수를 찾는 것이다!

우선 가장 먼저 떠오르는 해결방법은 브루드포스로 1 부터 계속 올라가면서 threshold 보다 작아지는 케이스를 찾으면 될 것이다!

시간 복잡도를 계산해보면 우선 nums를 모두 나눠야하니 O(5 * 10^4) 기준으로 가장 최악의 경우, threshold가 10^6이고, 가장 작은 수가 10^6인 경우,

O(5 * 10^4 * 10^6)이니까 O(5 * 10^10)이 된다!
매우 크기 때문에 나중에 시간 복잡도를 줄여야한다.

결국! Time Limit Exceeded가 떳다!

전체 탐색의 시간 복잡도를 줄이기 위해선 +1 대신 두배 를 하고, 더 큰 경우에는 줄이는 방식으로 하는 등이 있는데
제일 대표적인건 이진 탐색이다.

여기서 이진 탐색을 하기 위해선 어떻게 해야할까 보통의 이진 탐색은 가장 큰 값을 찾고, 그걸 기준으로 중간 값을 가지고 계산하는 것이다.

그럼 여기서 가장 큰 값으로 둘 만한건, nums의 최대값,

nums의 최대값을 구하는 시간복잡도 O(5 * 10^4), 이진 탐색의 최댓값은 10^6이고, 최솟값은 1 이니까 O(log(10^6))일 것이다. 그리고 5 * 10^4 만큼을 만복해야하니 O(5 * 10^4 + log(10^6))일 것이고

결국 O(5 * 10^4 * log(10^6)) 이 될 것이다! 확 작아지는군

와 이래도 타임아웃 뜨네??
"""
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        divisor = right

        while left <= right:
            mid = (left + right) // 2

            sum_of_division_results = sum(math.ceil(num / mid) for num in nums)
            
            if sum_of_division_results <= threshold:
                divisor = mid
                right = mid - 1
            else:
                left = mid + 1

        return divisor

