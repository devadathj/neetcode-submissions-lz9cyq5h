# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        nodes = deque()
        nodes.append(root)
        
        output = []

        while nodes:
            node = nodes.popleft()

            if node:
                nodes.append(node.left)
                nodes.append(node.right)
                output.append(str(node.val))
            else:
                output.append("None")

        print(output)
        return "_".join(output)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        node_values = deque(data.split("_"))

        root = TreeNode(int(node_values.popleft()))

        nodes = deque()
        nodes.append(root)

        while node_values:
            node = nodes.popleft()

            x = node_values.popleft()
            if x != "None":
                node.left = TreeNode(int(x))
                nodes.append(node.left)

            x = node_values.popleft()
            if x != "None":
                node.right = TreeNode(int(x))
                nodes.append(node.right)
        
        return root
