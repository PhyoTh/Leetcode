# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []

        stk = deque([root])
        while stk:
            level = []
            for node in list(stk):
                temp = stk.popleft()
                level.append(temp.val)
                
                if node.left:
                    stk.append(node.left)
                if node.right:
                    stk.append(node.right)
            result.append(level)

        return result