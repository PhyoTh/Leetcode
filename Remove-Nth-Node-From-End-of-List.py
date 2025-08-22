# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Odd case
n = 2
-1 -> 1 -> 2
|          |
s          f
i = 2

Even case
n = 2
1 -> 2 -> 3 -> 4 -> 5 -> 6
               |         |
               s         f
i = 3
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None:
            return head
        if head.next is None and n > 0:
            return None
        
        temp = ListNode(-1)
        temp.next = head

        slow = temp
        fast = temp
        for i in range(n):
            fast = fast.next
        
        while fast.next is not None:
            slow = slow.next # now slow is at the node before the nth
            fast = fast.next
        
        slow.next = slow.next.next
        return temp.next