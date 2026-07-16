# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = TreeNode(-1)

        def find(root) -> bool:
            nonlocal result
            if not root:
                return False

            found_one = root.val in (p.val, q.val)

            left = find(root.left)
            right = find(root.right)

            if (found_one and (left or right)) or (left and right):
                result = root
            
            return left or right or found_one

        find(root)
        return result