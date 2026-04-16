1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        if len(lists) == 0:
9            return None
10        if len(lists) == 1:
11            return lists[0]
12
13        result = self.mergeTwoSortedLinkedList(lists[0], lists[1])
14        for third in lists[2:]:
15            result = self.mergeTwoSortedLinkedList(result, third)
16        return result
17        
18    def mergeTwoSortedLinkedList(self, link1: ListNode, link2: ListNode) -> ListNode:
19        dummy = ListNode(-1)
20        walker = dummy
21        while link1 and link2:
22            if link1.val <= link2.val:
23                walker.next = link1
24                link1 = link1.next
25            else:
26                walker.next = link2
27                link2 = link2.next
28            walker = walker.next
29        
30        if link1 == None:
31            walker.next = link2
32        elif link2 == None:
33            walker.next = link1
34        return dummy.next