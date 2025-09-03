# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
        5
    /       \
    2         7
/      \     /   \
1       3    6    8

# iterative
level-Q: 5
Child-Q: 2 7
Result: 

level-Q: 2 7
Child-Q: 1 3 6 8
Result: 5


# recursive
V L R
5 2 7

2 1 3
7 6 8

1 n n
3 n n
6 n n
8 n n

q : 1
'''
class Solution(object):
    '''
    iterative approach
    '''
    # def levelOrder(self, root):
        # if root is None:
        #     return []

        # from collections import deque
        # level_q = deque([root]) # 9 20
        # result = [] # 3

        # while level_q: # iterate each level
        #     level = [] 

        #     for _ in range(len(level_q)): # iterate the whole level
        #         current = level_q.popleft()
        #         level.append(current.val)

        #         if current.left:
        #             level_q.append(current.left)
        #         if current.right:
        #             level_q.append(current.right)

        #     result.append(level)

        # return result

    '''
    recursive approach
    '''
    def levelOrder(self, root):
        if root is None:
            return []
        result = []

        self.level_traverse(root, 0, result)

        return result

    def level_traverse(self, root, level, result):
        if len(result) == level:
            result.append([])
        
        result[level].append(root.val)

        if root.left:
            self.level_traverse(root.left, level + 1, result)
        if root.right:
            self.level_traverse(root.right, level + 1, result)
        
        return 