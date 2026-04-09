# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        previous = slow.next = None

        while right:
            temp_node = right.next
            right.next = previous
            previous = right
            right = temp_node

        left = head
        while left and previous:
            act_left = left.next
            act_right = previous.next
            left.next = previous
            previous.next = act_left
            left = act_left
            previous = act_right
        


