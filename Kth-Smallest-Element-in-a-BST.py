# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        if root is None:
            return -1

        self.inOrderList = []
        self.inOrderTraversal(root)
        return self.inOrderList[k-1]
    
    def inOrderTraversal(self, root):
        if root is None:
            return
            
        self.inOrderTraversal(root.left)
        self.inOrderList.append(root.val)
        self.inOrderTraversal(root.right)