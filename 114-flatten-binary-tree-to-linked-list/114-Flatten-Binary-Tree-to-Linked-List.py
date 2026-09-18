# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        if not root:
            return None
        
        left = root.left
        right = root.right

        if left:
            self.flatten(root.left)
        if right:
            self.flatten(root.right)
        
        root.left = None
        root.right = left

        walker = root
        while walker.right:
            walker = walker.right
        walker.right = right