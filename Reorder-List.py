# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        # practice
        # reverse the half of the list
        # and merge the two halfs
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, walker = None, slow
        while walker:
            front = walker.next
            walker.next = prev

            prev = walker
            walker = front

        while prev.next:
            t1, t2 = head.next, prev.next
            head.next = prev
            prev.next = t1

            head, prev = t1, t2