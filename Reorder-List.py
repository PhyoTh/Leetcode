1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        if head is None or head.next is None:
9            return
10
11        slow = head
12        fast = head
13        # find the middle
14        while fast and fast.next:
15            slow = slow.next
16            fast = fast.next.next
17        
18        # reverse second half of list
19        prev = None
20        while slow:
21            nxt = slow.next
22            slow.next = prev
23            prev = slow
24
25            slow = nxt
26        
27        # merge
28        walker = head
29        while prev.next:
30            t1, t2 = head.next, prev.next
31            head.next = prev
32            prev.next = t1
33
34            head, prev = t1, t2