# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
root = 2
root.left = {
    root = 1
    root.left = None
    root.right = None
}
root.right = {
    root = 
}

'''
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return root
        left = root.left 
        right = root.right

        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root