1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseLinkedList(self, head, prev, after):
8        end = after
9        while head and head != end:
10            temp = head.next
11            head.next = after
12            after = head
13
14            head = temp
15            if prev and head != end:
16                prev.next = head
17        return after
18
19    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
20        if left == right:
21            return head
22
23        walker = head
24        count = 1
25        prev = None
26        while walker and right > count:
27            if left > count:
28                prev = walker
29            
30            walker = walker.next
31            count += 1
32        
33        if count == 1:
34            return head
35        
36        start = head if prev == None else prev.next
37        new_head = self.reverseLinkedList(start, prev, walker.next)
38        return new_head if prev == None else head