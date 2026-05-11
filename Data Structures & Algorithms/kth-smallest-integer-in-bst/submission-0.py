# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.counter = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return root

        left = self.kthSmallest(root.left, k)

        self.counter += 1

        if self.counter == k:
            return root.val
        
        right = self.kthSmallest(root.right, k)

        return left or right
        