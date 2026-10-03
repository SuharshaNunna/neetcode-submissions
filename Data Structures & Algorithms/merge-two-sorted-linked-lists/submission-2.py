# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
given list 1  and list 2 
goal merge both lists -> return one sorted list with all compeoents from both lists 

- there can be duplicates 
     need to make sure the comparison of the node is < or = 
nulls do not count 
empty lists are a posibiliyy 
if a list is empyty just return the other list 

pick a list to build off of whicheven one has the smallest head, if its = then defalt 1 
compare the node of lis one to node of 2
whichever one is smaller goes next 
    iterate that list to the secodn ponter 

Input: list1 = [1,2,4], list2 = [1,3,5]
1 
list1 = 2,4], list2 = [1,3,5]
1 1
list1 = [2,4], list2 = [,3,5]
112
list1 = [,4], list2 = [,3,5]
1123
list1 = [,4], list2 = [,5]
11234
list1 = [], list2 = [,5]
11234

at each step compare which head is the smallest, then add to new list, delete from old list 
if a lsit becomes empty, append the end of the linked list to the new list and return 
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        dummy= ListNode()
        newlist = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                newlist.next = list1
                list1= list1.next
            else:
                newlist.next = list2
                list2= list2.next
            newlist= newlist.next
        if list1:
            newlist.next = list1
        if list2:
            newlist.next = list2
        return dummy.next



        