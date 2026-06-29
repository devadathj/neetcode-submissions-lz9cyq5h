"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        node_register = {}
        output = start = Node(-999)
        head_start = head

        while head is not None:
            new_node = Node(head.val)
            start.next = new_node
            start = start.next
            node_register[head] = start
            head = head.next 

        start = output.next
        head = head_start
        while start is not None:
            start.random = node_register[head.random] if head.random else None
            start = start.next
            head = head.next

        return output.next

