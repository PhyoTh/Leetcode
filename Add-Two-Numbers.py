1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        head = walker = None
9
10        walker1 = l1
11        walker2 = l2
12        carry = 0
13        while walker1 or walker2:
14            walker1_val = walker1.val if walker1 else 0
15            walker2_val = walker2.val if walker2 else 0
16
17            total = walker1_val + walker2_val + carry
18            carry = total // 10
19            total = total % 10
20
21            new_node = ListNode(total)
22            if head is None:
23                head = walker = new_node
24            else:
25                walker.next = new_node
26                walker = walker.next
27
28            if walker1:
29                walker1 = walker1.next
30            if walker2:
31                walker2 = walker2.next
32        
33        if carry > 0:
34            walker.next = ListNode(carry)
35        return head