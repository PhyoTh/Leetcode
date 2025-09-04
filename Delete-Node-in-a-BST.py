# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def successor(self, root):
        walker = root.right
        while walker.left:
            walker = walker.left
        return walker

    def predecessor(self, root):
        walker = root.left
        while walker.right:
            walker = walker.right
        return walker

    def deleteNode(self, root, key):
        if root is None:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None and root.right is None: # case1: if its leaf
                return None
            elif root.left is None: # case2: if there is right child
                successor_node = self.successor(root)
                root.val = successor_node.val
                root.right = self.deleteNode(root.right, successor_node.val)
            else: # case3: if there is left child
                predecessor_node = self.predecessor(root)
                root.val = predecessor_node.val
                root.left = self.deleteNode(root.left, predecessor_node.val)
        return root