# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root) -> int:
            if not root:
                return 0
            
            left = maxDepth(root.left) + 1
            right = maxDepth(root.right) + 1
            self.diameter = max(self.diameter, left + right - 2)
            return max(left, right)

        maxDepth(root)
        return self.diameter