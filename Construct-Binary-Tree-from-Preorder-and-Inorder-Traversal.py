# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
The idea is that for preorder its root->left->right
for inorder its left->root->right

so, when we build the trees, the elements in the preorder are the roots
and, in order will tell us about when to split the right and left subtree


preorder = [3, 9, 20, 15, 7]
            ^
inorder = [9, 3, 15, 20, 7]

preorder_index = 1
inorder_map = { 9:0, 3:1, 15:2, 20:3, 7:4 }
'''
class Solution(object):
    def buildTree(self, preorder, inorder):
        self.preorder_index = 0
        self.inorder_map = {}
        for index, value in enumerate(inorder):
            self.inorder_map[value] = index
        
        def arrayTotree(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.preorder_index]
            root = TreeNode(root_val)
            self.preorder_index += 1

            root.left = arrayTotree(left, self.inorder_map[root_val] - 1)
            root.right = arrayTotree(self.inorder_map[root_val] + 1, right)
        
            return root
        return arrayTotree(0, len(inorder) - 1)