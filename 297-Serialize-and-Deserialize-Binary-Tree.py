# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
import math
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = ''
        que = deque([root])
        while que:
            for _ in range(len(que)):
                node = que.popleft()

                if not node:
                    result += 'N|'
                    continue

                result += str(node.val) + '|'

                left = node.left if node.left else None
                right = node.right if node.right else None

                que.append(left)
                que.append(right)

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split('|')[:-1]
        
        root = TreeNode(data[0]) if data[0] != 'N' else None
        que = deque([root])
        i = 1
        while i < len(data):
            node = que.popleft()
                    
            node.left = TreeNode(data[i]) if data[i] != 'N' else None
            if node.left:
                que.append(node.left)

            if i + 1 < len(data):
                node.right = TreeNode(data[i + 1]) if data[i + 1] != 'N' else None
                if node.right:
                    que.append(node.right)

            i += 2

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))