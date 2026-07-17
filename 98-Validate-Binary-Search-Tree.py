# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
            5
        /       \
        4       6
              /   \
             3     7
Expected: false?
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, low, high) -> bool:
            if not root:
                return True
            elif root.val <= low or root.val >= high:
                cur = False
            else:
                cur = True
            
            left = valid(root.left, low, root.val)
            right = valid(root.right, root.val, high)
            
            return left and right and cur

        return valid(root, float('-inf'), float('inf'))