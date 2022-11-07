# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

문제를 정리해보겠습니다.

linked list가 들어오고 그 리스트에서 중복값을 제거한 후에 다시 링크드 리스트로 반환하는거죠?

input - linked list
output - linked list

여기서 중요한 것은 중복값을 하나만 남겨놓는 것이 아니라, 아예 없애버리는 거 맞습니까?

1,2,3,3,4,4,5 -> 1,2,5 (3,4 는 삭제)

, -> None

1,1,1,1,1,1 -> None

=========================================================================

우선 linked list의 모든 node를 탐색하여 별도의 hash map에 저장합니다.

이때 키는 node의 value로 하고, map의 value는 True, False로 합니다.

이때 디폴트 값은 True로 하고, 만약 또 다른 중복값이 나오면 False로 바꿉니다.

모든 node 탐색이 끝나면, 이 map을 다사 탐색해서 value가 True인 것들만 linked list로 만들어서 반환합니다.


1,2,3,3,4,4,5
            |

-> {1 : True, 2 : True, 3 : False, 4 : False, 5 : True}

링크드 리스트는 반대로 생성되는게 편합니다.

map을 desc로 정렬한 후, 키를 기반으로 새로운 Linked list를 만듭니다.


{5: True, 4: False, 3: False, 2: True, 1 : True}

->[1,2,5]

"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.make_hash_map_to_list(self.make_value_hash_map(head))
    

    def make_value_hash_map(self, head: Optional[ListNode]) -> list:
        hash_map = {}
        target = head
        while target:
            v = target.val

            if v in hash_map:
                hash_map[v] = False
            else:
                hash_map[v] = True
            
            target = target.next
        return hash_map


    def make_hash_map_to_list(self, hash_map: dict) -> ListNode:
        results = sorted(hash_map.items(), key = lambda x : x[0], reverse = True)
        tail = None

        for result in results:
            if result[1]:
                if tail is None:
                    tail = ListNode(result[0], None)
                else:
                    target = ListNode(result[0], tail)
                    tail = target
            
        return tail
        