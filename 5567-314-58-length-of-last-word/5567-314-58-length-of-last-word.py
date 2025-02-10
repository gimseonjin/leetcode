class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 공백을 기준으로 문자열을 분리합니다.
        words = s.split(" ")
        
        # 빈 문자열을 제외한 단어들만 남깁니다.
        non_empty_words = list(filter(lambda word: len(word) > 0, words))
        
        # 마지막 단어의 길이를 구합니다.
        last_word_length = len(non_empty_words[-1])
        
        return last_word_length
        