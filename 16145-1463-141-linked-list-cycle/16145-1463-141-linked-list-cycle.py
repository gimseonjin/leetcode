# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        visited_nodes = []

        target = head
        while True:
            if target in visited_nodes:
                return True

            visited_nodes.append(target)
            if target.next is not None:
                target = target.next
            else:
                return False