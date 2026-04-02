1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        if head is None:
10            return False
11
12        slow = head
13        fast = head.next
14        if fast is None:
15            return False
16
17        while slow != fast:
18            if slow is None or fast is None or fast.next is None:
19                return False
20            slow = slow.next
21            fast = fast.next.next
22        return True
23        