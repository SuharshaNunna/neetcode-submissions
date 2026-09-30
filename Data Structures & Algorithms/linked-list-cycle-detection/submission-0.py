# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # index is the the index the last node points to (-1) is null 
        # can use two pointers ( one moving fast and one moving slow)
        # stopping condition is when fast point and the next value of fast arw not valid 
        # if none is the value of the node at that point return false, if not return true 
        fast,slow=head,head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast== slow:
                return True
            
        return False     
  
        