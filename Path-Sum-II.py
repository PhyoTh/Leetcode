1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
9        result = []
10
11        def dfs(root, targetSum, path: List[int]):
12            if root == None:
13                return
14
15            path.append(root.val)
16            if targetSum - root.val == 0 and not root.left and not root.right:
17                result.append(path.copy())
18            
19            dfs(root.left, targetSum - root.val, path)
20            dfs(root.right, targetSum - root.val, path)
21            path.pop()
22        
23        dfs(root, targetSum, list())
24        return result