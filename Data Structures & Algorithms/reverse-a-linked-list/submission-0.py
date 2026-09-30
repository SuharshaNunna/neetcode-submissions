# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # to reverse a linked list  make the current node point to previous instead of the 
        # next node and move though the list 
        prev = None
        curr = head
        while curr != None:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp 
        return prev
        