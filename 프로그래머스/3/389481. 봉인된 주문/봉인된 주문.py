"""
아 26진수다
"""
def int_to_base26(n: int) -> str:
    digits = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    while n:
        n, remainder = divmod(n - 1, 26)
        result = digits[remainder] + result
    return result

def base26_to_int(s: str) -> int:
    digits = "abcdefghijklmnopqrstuvwxyz"
    n = 0
    for char in s:
        n = n * 26 + (digits.index(char) + 1)
    return n


def solution(n, bans):
    
    to_delete = []
    for ban in bans:
        spell_num = base26_to_int(ban)
        to_delete.append(spell_num)
    
    for delete in sorted(to_delete):
        if delete <= n:
            n += 1
            
    return int_to_base26(n)