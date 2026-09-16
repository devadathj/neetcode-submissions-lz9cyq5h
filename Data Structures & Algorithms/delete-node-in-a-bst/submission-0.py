# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def deletenode(node, key):
            if not node:
                return
            
            if node.val > key:
                node.left = deletenode(node.left, key)
            elif node.val < key:
                node.right = deletenode(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    successor = node.right
                    
                    while successor.left:
                        successor = successor.left

                    node.val = successor.val
                    node.right = deletenode(node.right, node.val)

            return node

        return deletenode(root, key)