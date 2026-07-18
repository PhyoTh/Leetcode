# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = -1
        rank = 0
        def inOrder(root) -> int:
            nonlocal result, rank
            if not root:
                return 0
            elif result != -1:
                return -1
            
            left = inOrder(root.left)
            rank += 1
            if rank == k:
                result = root.val
            right = inOrder(root.right)

            return rank
        
        inOrder(root)
        return result