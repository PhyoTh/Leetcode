# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
0 -> 1 -> 2 -> 3 -> None, n = 2
|         |

0 -> 1 -> 2 -> 3 -> 4 -> None, n = 2
|         |
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        prev_slow = None
        while n > 0 and fast:
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            prev_slow = slow
            slow = slow.next
        
        if prev_slow:
            prev_slow.next = slow.next
        else:
            head = head.next
        
        return head