"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        new_root = Node(node.val)
        node_map = {node: new_root}

        que = deque([node])
        seen = set()
        while que:
            root = que.popleft()
            seen.add(root)

            for neighbor in root.neighbors:
                if neighbor in seen:
                    continue

                if neighbor not in node_map:
                    new_node = Node(neighbor.val)
                    node_map[neighbor] = new_node
                else:
                    new_node = node_map[neighbor]

                node_map[root].neighbors.append(new_node)
                new_node.neighbors.append(node_map[root])

                que.append(neighbor)
            
        return new_root
