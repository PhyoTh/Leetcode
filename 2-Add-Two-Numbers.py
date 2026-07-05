# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(-1)
        new_walker = new_head

        carry = 0
        while l1 or l2:
            total = 0
            total += l1.val if l1 else 0
            total += l2.val if l2 else 0
            total += carry if carry else 0

            carry = total // 10
            total = total % 10

            new_walker.next = ListNode(total)

            new_walker = new_walker.next

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if carry:
            new_walker.next = ListNode(carry)

        return new_head.next