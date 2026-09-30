# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
# traverse the node then left and right though recursion, if the node is the same value keep going if not exit early and return false 
       #note for trees: dont need to set a value to the head can just do tree.val or tree.next and such 
        if not p and not q:
            return True
            # if both are null
        if  not p or not q or p.val != q.val:
            return False 
            # if only one is null or not the same 
        else:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    

        