1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
9        if not root:
10            return False
11        elif targetSum - root.val == 0 and root.right == None and root.left == None:
12            return True
13        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum  - root.val)