"""
제일 쉬운 방법은 for문 두번 돌면서 모든 케이스를 검사하는 것이다.

그러면 우선 O(N^2)이 들 것이고 판단하는데 O(N)이 들어서 O(N^2 + N)이다.

흠 이걸 조금 효율적으로 풀어보려면, palindromic은 결국 반대로 했을 때 같은 것

그렇기 때문에 이미 palidoromic 좌우에 같은 글자가 오면 그것도 palidoromic이고, 더 긴 것이다.

여기서 중요한 건, 홀수인 것이랑 짝수인 것 두 개가 있다.

그렇기 때문에 cursor을 옮길 때, 내가 기준인 것과, 내 옆의 것을 같이 넣어서 기준인 것 두개를 만들어야 한다.

그리고 길이를 찾는 게 아니라 그 string을 찾아야 하기 때문에 최대 길이의 반을 나눠서 left, right 부분을 잘 잘라야한다.

아 그리고 빈 배열이나 한 개만 있는 경우에는 그냥 그걸 반환하는게 더 빠르다
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s

        left, right = 0, 0

        for i in range(len(s)):
            odd_pal_length = self.expandAroundCenter(s, i, i)
            even_pal_length = self.expandAroundCenter(s, i, i + 1)

            cur_max_len = odd_pal_length if odd_pal_length > even_pal_length else even_pal_length

            # 최대 길이 갱신
            if cur_max_len > right - left:
                left = i - (cur_max_len - 1) // 2
                right = i + cur_max_len // 2

        return s[left:right+1]
        
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        """
        좌우 인덱스(left, right)를 중심으로 Palindrome을 확장하면서 
        Palindrome의 길이를 반환하는 함수

        여기서 좌우 인덱스의 최대 길이는 각각 0과 s의 길이이고, 양 옆이 같다는 조건을 넣어야한다.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # while문을 탈출할 때 left와 right는 실제 팰린드롬 범위를 벗어나 있으므로,
        # 팰린드롬 길이는 (right - left - 1)
        return right - left - 1