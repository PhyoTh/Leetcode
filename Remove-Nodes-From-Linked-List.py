1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    # using stack
8    '''
9    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
10        stack = []
11        
12        walker = head
13        while walker:
14            stack.append(walker)
15            walker = walker.next
16        
17        maximum = stack.pop()
18        result = ListNode(maximum.val)
19        while stack:
20            node = stack.pop()
21            if node.val < maximum.val:
22                continue
23            else:
24                maximum = node
25                new_node = ListNode(maximum.val, result)
26                result = new_node
27
28        return result
29    '''
30
31    # reverse the linked list twice (space optimization)
32    def reverseList(self, head):
33        prev = nxt = None
34        current = head
35        while current:
36            nxt = current.next
37            current.next = prev
38            prev = current
39
40            current = nxt
41        return prev
42
43    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
44        if head is None:
45            return None
46
47        # reverse the linked list
48        head = self.reverseList(head)
49
50        # traverse and decline when seen max
51        maximum = 0
52        prev = None
53        current = head
54        while current:
55            maximum = max(current.val, maximum)
56
57            if current.val < maximum:
58                prev.next = current.next
59            else:
60                prev = current
61
62            current = current.next
63
64        return self.reverseList(head)