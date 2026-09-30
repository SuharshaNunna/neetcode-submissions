# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs or queue
        # traverse by level or count up by number of nodes visited in pathway, if max is replaced update
        # recursion 
        # check if there is a child, if there is (left or right) increase count by one 
        # put the child node in the recursive call 
    
        if root:
            return( 1+ max(self.maxDepth(root.left), self.maxDepth(root.right)))
        else:
            return 0 
      
     

        
            
