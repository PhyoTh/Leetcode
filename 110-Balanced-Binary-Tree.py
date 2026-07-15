# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        def depth(root) -> int:
            if not root:
                return 0
            
            left = depth(root.left) + 1
            right = depth(root.right) + 1
            if abs(left - right) > 1:
                self.balance = False
            return max(left, right)

        depth(root)
        return self.balance