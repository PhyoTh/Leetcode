# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = float('-inf')
        stk = [(root, 1)]
        while stk:
            node, depth = stk.pop()
            result = max(result, depth)
            
            if node.right:
                stk.append((node.right, depth + 1))
            if node.left:
                stk.append((node.left, depth + 1))

        return result