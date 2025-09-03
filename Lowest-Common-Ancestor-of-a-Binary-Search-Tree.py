# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val > root.val and q.val > root.val: # search on the right subTree
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val: # serach on the left subTree
            return self.lowestCommonAncestor(root.left, p, q)
        else: # we have reached the divider and the root is the LCA
            return root