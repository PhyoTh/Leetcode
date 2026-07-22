# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        here = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:here + 1], inorder[0:here + 1])
        root.right = self.buildTree(preorder[here + 1:], inorder[here + 1:])

        return root