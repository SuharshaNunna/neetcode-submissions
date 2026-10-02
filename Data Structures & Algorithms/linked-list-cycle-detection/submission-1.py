# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
 given head 
 return bool 
 return true for a cycle in a linked list

 cycle definition:
 at least one node in the list can be visited again by following the next pointer

 index
end of cycle point to index 
-1 means no cycle 
last node points to that index ith  node 

two pointer 
starting pointer at first node 
second pointer at second node
iterate first and second pointer to the next
if second is ever behind first = cycle 
if second ever reaches null == no cycle 

other cases:
empty list == no cycle
one node == first poijner set, if node -> next == -1 == no cycle, any other cycle
two nodes 
 head = [1,2], index = -1
 1st pointer =1 
 2nd pointer =2 
 iterate 1st pointer is now 2 ; 2cnt pointer is -1 
 termniate 

 constraints 
 0 <= Length of the list <= 1000.  
 worst case second pointer has to go to each element-> O(n)

 '''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        first, second = head, head 
        while second and second.next :
                first = first.next
                second = second.next.next
                if first == second :
                    return True 
        return False

        