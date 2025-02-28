def number_to_spell(index: int) -> str:
    """정수 인덱스를 주문 문자열(26진수)로 변환"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    spell = ""
    while index:
        index, remainder = divmod(index - 1, 26)
        spell = alphabet[remainder] + spell
    return spell

def spell_to_number(spell: str) -> int:
    """주문 문자열(26진수)을 정수 인덱스로 변환"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = 0
    for char in spell:
        index = index * 26 + (alphabet.index(char) + 1)
    return index

def solution(order: int, banned_spells: list) -> str:
    """삭제된 주문을 제외하고 order번째 주문을 반환"""
    
    banned_indices = [spell_to_number(spell) for spell in banned_spells]
    banned_indices.sort()
    
    for banned in banned_indices:
        if banned <= order:
            order += 1
            
    return number_to_spell(order)
