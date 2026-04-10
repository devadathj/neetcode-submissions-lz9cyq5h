# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        output_start = output = ListNode()

        while True:

            minval = float("inf")
            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val < minval:
                        minval = lists[i].val
                        minvallist = i

            if minval != float("inf"):
                output.next = lists[minvallist]
                output = output.next
                lists[minvallist] = lists[minvallist].next
            else:
                return output_start.next


