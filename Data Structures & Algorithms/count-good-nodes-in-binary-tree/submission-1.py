# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.output = 0

        def check_val(node, chain_max):

            if not node:
                return

            if node.val >= chain_max:
                self.output += 1
                chain_max = node.val

            check_val(node.left, chain_max)
            check_val(node.right, chain_max)

        check_val(root, -101)

        return self.output
            