# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        start = dummy

        for _ in range(left - 1):
            start = start.next
        
        curr = start.next
        prev = None
        for i in range(left, right + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        start.next.next = curr
        start.next = prev

        return dummy.next