# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if head is None or head.next is None:
            return

        # step 1: find the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse the second half of the list
        prev = None
        curr = slow # right now slow is at the middle of the list
        while curr:
            front = curr.next
            curr.next = prev

            prev = curr
            curr = front

        # step 3: merge the two halfs of the list
        first = head
        second = prev
        while second.next: # we can do this for this problem because we know that they both have same length or second half is the smaller one
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1

            first, second = t1, t2