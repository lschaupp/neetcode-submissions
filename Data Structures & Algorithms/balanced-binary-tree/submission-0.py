# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        def check(node):
            if not node:
                return 0, True

            height_left, balanced_left = check(node.left)
            height_right, balanced_right = check(node.right)

            height = 1 + max(height_left, height_right)
            balanced = False
            if abs(height_left - height_right) <= 1 and balanced_left and balanced_right:
                balanced = True
            return height, balanced
        return check(root)[1]
                
        