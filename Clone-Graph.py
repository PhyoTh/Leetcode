
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        clone_dict = {node : Node(node.val)}
        explore = deque([node])

        while explore:
            current_node = explore.popleft()
            current_clone = clone_dict[current_node]

            for neighbor in current_node.neighbors:
                if neighbor not in clone_dict:
                    clone_dict[neighbor] = Node(neighbor.val)
                    explore.append(neighbor)

                current_clone.neighbors.append(clone_dict[neighbor])
    
        return clone_dict[node]