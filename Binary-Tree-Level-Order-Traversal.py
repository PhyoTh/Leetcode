1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if root is None:
10            return []
11
12        from collections import deque
13        result = []
14        que = deque([root])
15
16        while que:
17            level = []
18
19            n = len(que)
20            for _ in range(n):
21                node = que.popleft() # pop from left
22                level.append(node.val)
23
24                if node.left:
25                    que.append(node.left) # append from right
26                if node.right:
27                    que.append(node.right)
28
29            result.append(level.copy())
30        
31        return result
32            