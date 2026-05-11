# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        output = []
        nodes = [[root]]

        for i in nodes:
            current_output = []
            next_nodes = []
            for j in i:
                current_output.append(j.val)
                if j.left:
                    next_nodes.append(j.left)
                if j.right:
                    next_nodes.append(j.right)

            output.append(current_output)
            if next_nodes:
                nodes.append(next_nodes)
        
        return output


