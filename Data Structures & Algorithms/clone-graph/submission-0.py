"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        if not node:
            return None

        check = {}

        def copy_node(node):
            root = Node(node.val)
            check[node] = root

            for i in node.neighbors:
                if i not in check:
                    copy_node(i)
                root.neighbors.append(check[i])                    

            return root

        return copy_node(node)



