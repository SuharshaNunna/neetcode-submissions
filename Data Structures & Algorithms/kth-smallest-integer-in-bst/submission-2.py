# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
# returning kth smallest 
# naitve would be to do left root right traveral ( incrementing counter by 1) untill it reaches k 
# basically going from smallest to largest and keeping track of indexes 
# problem : need to traverse all the way to left and then start counting 
        res = root.val
        index = k 
        def trav(node):
            nonlocal index, res
            if not node:
                return 
            trav(node.left)
            index -= 1
            if index == 0:
                res = node.val
                return 
            trav(node.right)
        trav(root) 
        return res 
        

        
        
        