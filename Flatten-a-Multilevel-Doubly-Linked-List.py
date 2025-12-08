1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val, prev, next, child):
5        self.val = val
6        self.prev = prev
7        self.next = next
8        self.child = child
9"""
10
11class Solution:
12    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
13        
14        def flatout(node): # returns last node
15            if node is None:
16                return node
17
18            last = node
19            walker = node
20            while walker:
21                last = walker
22
23                if walker.child:
24                    next_node = walker.next
25                    child_node = walker.child
26                    last_child_node = flatout(walker.child)
27
28                    walker.next = child_node
29                    child_node.prev = walker
30                    walker.child = None
31                    
32                    if next_node:
33                        last_child_node.next = next_node
34                        next_node.prev = last_child_node
35                    
36                    last = last_child_node
37
38                walker = walker.next
39
40            return last
41
42        flatout(head)
43        return head