# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.output = float("-inf")

        def sub_max(root):

            if not root:
                return float("-inf")

            left = sub_max(root.left)
            right = sub_max(root.right)

            node_sum = max(root.val, root.val + left, root.val + right)
            self.output = max(self.output, node_sum, root.val + left + right)

            return node_sum

        sub_max(root)
        return self.output
