# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.last_val = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        if not self.isValidBST(root.left):
            return False

        if self.last_val is not None and root.val <= self.last_val:
            return False
        
        self.last_val = root.val
        
        if not self.isValidBST(root.right):
            return False
        
        return True
