# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balance_check(node):

            if not node:
                return 0

            left = balance_check(node.left)
            right = balance_check(node.right)

            if left is False or right is False:
                return False
            check = abs(left - right)

            if check > 1:
                return False
            
            return 1 + max(left, right)

        output = balance_check(root)

        return output is not False