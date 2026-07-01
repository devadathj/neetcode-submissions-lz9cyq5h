# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        output = prev_tail = ListNode(0, head)

        curr = head
        while True:
            temp_head = curr

            for _ in range(k):
                if temp_head:
                    temp_head = temp_head.next
                else:
                    return output.next

            curr_head = previous = curr
            curr = curr.next
            for _ in range(k - 1):
                
                temp_next = curr.next
                curr.next = previous
                previous = curr
                curr = temp_next

            prev_tail.next = previous
            curr_head.next = curr
            prev_tail = curr_head
            

            


            