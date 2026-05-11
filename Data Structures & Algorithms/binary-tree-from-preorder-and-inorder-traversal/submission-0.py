# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return []

        inorder_map = {val:index for index, val in enumerate(inorder)}

        self.preindex = 0

        def dfs(left, right):

            if left > right:
                return None

            root = TreeNode(preorder[self.preindex])            
            mid = inorder_map[preorder[self.preindex]]

            self.preindex += 1
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(preorder) - 1)