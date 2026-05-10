# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True

        if not root:
            return False
        
        if self.check_match(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def check_match(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if root and subRoot and root.val == subRoot.val:
            return self.check_match(root.left, subRoot.left) and self.check_match(root.right, subRoot.right)
        if not root and not subRoot:
            return True
        else:
            return False

