class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def check(nodeA, nodeB):

            if not nodeA and not nodeB:
                return True

            if not nodeA or not nodeB or nodeA.val != nodeB.val:
                return False

            right = check(nodeA.right, nodeB.right)
            left = check(nodeA.left, nodeB.left)

            return left and right

        return check(p, q)