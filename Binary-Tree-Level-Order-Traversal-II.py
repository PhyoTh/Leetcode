1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
9        # can do the same with previous BFS iteratative method
10        if root is None:
11            return []
12        
13        levels = []
14        def dfs(root: Optional[TreeNode], level: int):
15            if len(levels) == level:
16                levels.append([])
17            
18            levels[level].append(root.val)
19            if root.left:
20                dfs(root.left, level + 1)
21            if root.right:
22                dfs(root.right, level + 1)
23        dfs(root, 0)
24        return levels[::-1] # reverse the levels