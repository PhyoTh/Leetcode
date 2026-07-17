# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        good_counter = 0
        stk = [(root, root.val)]
        while stk:
            node, min_threshold = stk.pop()

            if node.val >= min_threshold:
                good_counter += 1

            if node.right:
                stk.append((node.right, max(min_threshold, node.val)))
            if node.left:
                stk.append((node.left, max(min_threshold, node.val)))

        return good_counter