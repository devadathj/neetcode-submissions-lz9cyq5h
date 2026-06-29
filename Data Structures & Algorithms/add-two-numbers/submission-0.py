# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        output_start = output = ListNode()
        extra = 0
        while True:
            if l1 and l2:
                digit_val = l1.val + l2.val + extra
                l1 = l1.next
                l2 = l2.next
            elif l1:
                digit_val = l1.val + extra
                l1 = l1.next
            elif l2:
                digit_val = l2.val + extra
                l2 = l2.next
            else:
                if extra:
                    output.next = ListNode(extra)
                    
                return output_start.next

            extra = digit_val // 10
            output.next = ListNode(digit_val % 10)
            output = output.next
