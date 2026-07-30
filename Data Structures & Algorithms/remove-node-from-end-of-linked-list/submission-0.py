# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        [1]= length  - n + 1
         ^ 
         ^

        cases: 3.next = None (end)
        middle: 2.next = 2.next.next
        first: head = head.next

        lead
        follwer:
        before I move flower: i ahveto store somewher

        """

        # lead
        lead = head
        count = n

        while count > 1:
            lead = lead.next
            count -= 1
        
        # move follower aldn lead sim
        prev = None
        follower = head
        while lead.next:
            lead = lead.next
            prev = follower
            follower = follower.next

        # middle
        if prev and prev.next:
            prev.next = prev.next.next
        elif not prev:
            head = head.next

        return head
        



