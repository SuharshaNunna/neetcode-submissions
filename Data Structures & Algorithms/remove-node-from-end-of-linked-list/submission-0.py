# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # REQ: remove nth position node from end (ind= len(total)- n) and return whole list 
    # identify node that needs to be removed, store prev and next node, remove node 
    #a->b->c->d   
    #prev->next , curr->null, delete curr 
    # need to get length of list and identify pos in one pass through 
    # brute first 
        curr= head 
        count =0 
        while curr:
            count += 1
            curr = curr.next 
        idx = count - n 
        if idx == 0:
            return head.next
        curr = head 

        for i in range (idx-1 ):
            curr= curr.next
        curr.next= curr.next.next

        return head 

            