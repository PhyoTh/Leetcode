# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
        5
    /       \
   4         6
           /   \
          3     7
'''
class Solution(object):
    def isValidBST(self, root):
        # valid range (recursive approach)
        # return self.checkBST_recursive_range(root) # 8ms
        
        # valid range (iterative approach)
        # return self.checkBST_iterative_range(root) # 4ms
        
        # in order traversal (recursive approach)
        self.prev = float('-inf')
        return self.checkBST_recursive_inorder(root)

    '''
    valid range approach
    '''
    def checkBST_recursive_range(self, root, min_val = float('-inf'), max_val = float('inf')):
        if root is None:
            return True
        elif root.val <= min_val or root.val >= max_val:
            return False
        
        left = self.checkBST_recursive_range(root.left, min_val, root.val)
        right = self.checkBST_recursive_range(root.right, root.val, max_val)

        return left and right
    
    def checkBST_iterative_range(self, root):
        if root is None:
            return True

        from collections import deque
        level_q = deque([(root, float('-inf'), float('inf'))]) # tuple(node, min, max)

        valid = True
        while level_q:
            for _ in range(len(level_q)):
                current = level_q.popleft()
                if current[0].val <= current[1] or current[0].val >= current[2]:
                    valid = False

                if current[0].left:
                    level_q.append((current[0].left, current[1], current[0].val))
                if current[0].right:
                    level_q.append((current[0].right, current[0].val, current[2]))
            
        return valid

    '''
    the trick is that if we follow in order traversal, the prev is always smaller than the curent walker
    '''
    def checkBST_recursive_inorder(self, root):
        if root is None:
            return True
        
        left = self.checkBST_recursive_inorder(root.left)
        if root.val <= self.prev:
            return False
        self.prev = root.val
        right = self.checkBST_recursive_inorder(root.right)
        
        return left and right