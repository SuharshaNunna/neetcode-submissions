# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # could make a new linked list but may be better to just modify one as it iterates through two 
        # as we go through list 1 check list 2 if if the value is next in order store next as temp
        # and point to next list 
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val< list2.val :
            head= list1
            list1= list1.next
        else:
            head = list2
            list2=list2.next
        curr = head
        while list1 and list2:
            if list1.val < list2.val :
                curr.next=list1
                list1= list1.next
            else: 
                curr.next=list2
                list2= list2.next
            curr=curr.next
        if list2:
            curr.next= list2
        else:
            curr.next =list1
        return head


        