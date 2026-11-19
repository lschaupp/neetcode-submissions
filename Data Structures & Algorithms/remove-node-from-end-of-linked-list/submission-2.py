# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Approach: slow/fast pointer, once fast pointer reaches the end, fast pointer is n-steps away from the slow pointer. Use a dummy node for edge cases
        dummy = ListNode(-1)
        dummy.next = head

        slow = fast = dummy

        # Ahead the fast pointer by n steps
        for _ in range(n+1):
            fast = fast.next
        
        # Take both pointers ahead (sames steps)
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next


        
        