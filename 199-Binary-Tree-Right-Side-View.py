# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        que = deque([root])
        while que:
            for node in list(que):
                last = que.popleft()

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            result.append(last.val)
        return result