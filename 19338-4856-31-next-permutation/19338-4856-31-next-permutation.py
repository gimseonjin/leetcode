"""
보자 해석해보자면 permutation은 순열을 뜻한다.
그래서 nums를 받으면 그 배열의 다음 permutation를 찾는 것이다.
여기서 중요한 건, 사전 순서로 정렬해야한다.
1,2,3 이면 다음 순서는 1,3,2 인거시다!!

순열 알고리즘은 재귀로 만들 수 있다
            123
    123     213     321
  123 132 213 231 321 312

이걸 재귀로 만들 수 있지만 nums의 길이는 최대 100이 될거고
그러면 n! 되서 n^2이 된다

그리고 무엇보다 메모리를 먹게된다!
그러면 메모리를 그대로 사용하라는 제약이 안된다.
그러면 여기서 다음 순열을 찾는 알고리즘이 필요하다.

모든 수는 뒤에서 부터 찾는다.
1. a[i-1] < a[i] 인 수를 찾는다.
2. j >= i and a[j] > a[i-1] 인 수를 찾는다.
3. a[i-1]과 a[j]를 swap 한다.
4. 그 후 a[i]부터 끝까지 뒤집습니다.

1,4,2,3 -> 1,4,3,2
1,4,3,2 -> 2,1,3,4
2,1,3,4 -> 2,1,4,3
2,1,4,3 -> 2,3,1,4
"""

class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        # 배열이 내림차순이면(즉, 마지막 순열이면) 오름차순 정렬 후 반환
        if nums == sorted(nums, reverse=True):
            nums.sort()
            return

        n = len(nums)
        pivot = -1  # 오른쪽부터 처음으로 nums[i-1] < nums[i]를 만족하는 위치의 i-1 (피벗 인덱스)

        # 1. 오른쪽부터 순회하면서 피벗을 찾는다.
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot = i - 1
                break

        # 2. 피벗보다 큰 수 중에서 가장 작은 값을 찾는다. 오른쪽부터 탐색하면 첫 번째로 만나는 값이 된다.
        successor = -1  # 피벗과 swap할 대상의 인덱스
        for j in range(n - 1, pivot, -1):
            if nums[j] > nums[pivot]:
                successor = j
                break

        # 3. 피벗과 successor를 swap한다.
        nums[pivot], nums[successor] = nums[successor], nums[pivot]

        # 4. 피벗 다음 위치부터 끝까지의 부분 배열을 오름차순으로 정렬(뒤집기)
        nums[pivot + 1:] = nums[pivot + 1:][::-1]