# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []

        if not root:
            return output
        
        output.append(root.val)

        tracker = [root.right, root.left]

        while tracker:
            new_tracker = []
            switch = True
            for node in tracker:
                if node:
                    if switch:
                        output.append(node.val)
                        switch = False
                    new_tracker.append(node.right)
                    new_tracker.append(node.left)

            tracker = new_tracker

        return output

