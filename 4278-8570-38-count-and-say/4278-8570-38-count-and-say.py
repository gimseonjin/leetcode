"""
전형적인 재귀 문제이다!
실제로 n 도 30보다 작다!
즉! 철저한 재귀다!
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if(n == 1):
            return "1"
        
        prev_term = self.countAndSay(n - 1)
        count = 1
        result = ""

        for i in range(1, len(prev_term)):
            if prev_term[i] == prev_term[i-1]:
                count += 1
            else:
                result += f"{count}{prev_term[i-1]}"
                count = 1
        else:
            result += f"{count}{prev_term[-1]}"

        return result
        