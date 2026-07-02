# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.output = 0

        def extract_len(node):
            if not node:
                return 0

            left_max = right_max = 0
            if node.left:
                left_max = 1 + extract_len(node.left) 
            if node.right:
                right_max = 1 + extract_len(node.right)

            node_depth = left_max + right_max
            node_max = max(left_max, right_max)

            self.output = max(self.output, node_depth)
            return node_max

        extract_len(root)

        return self.output
            