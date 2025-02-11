"""

이 문제는 문자열 순서에 상관없이 같은 문자들로 구성된 문자열을 묶어서 반환하는 겁니다!

제일 쉬운 방법은 strs을 순회하면서 각 strs[i]를 정렬시킨 후, map 자료형을 통해 value에 배열을 넣어서 반환하는 방법입니다!

일단 시간 복잡도는

O(strs.length * strs[i].length)이고

O(N * M)이고 각각 최대 값이 10^4, 10^2 이니까 O(10^6) 정도니까 시간 복잡도는 충분할 것으로 보입니다.

놀랍게도 python에 defaultdict라는 자료형이 있다!!
key 값이 없는 경우 default로 list를 반환하는 것입니다.
코드가 매우 깔끔해질 거 같습니다.

"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for str in strs: 
            key = "".join(sorted(str))
            anagrams[key].append(str)

        return list(anagrams.values())