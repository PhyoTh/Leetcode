"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen_nodes = {}
        new_head = Node(-1)
        new_walker = new_head

        walker = head
        while walker:
            new_walker.next = Node(walker.val)
            new_walker = new_walker.next

            seen_nodes[walker] = new_walker

            walker = walker.next

        walker = head
        new_walker = new_head.next
        while walker:
            if walker.random:
                new_walker.random = seen_nodes[walker.random]

            walker = walker.next
            new_walker = new_walker.next

        return new_head.next