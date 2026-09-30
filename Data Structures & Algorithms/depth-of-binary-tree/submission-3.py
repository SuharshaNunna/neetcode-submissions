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

            #notes: when it comes to recursive calls, simplicity is usually better
            # no initiaizing of varibles unless it needs to be reset with every call 
            #can break the problem in smaller parts and use the same method to solve the rest
            #so recursive solution works

            #BFS solution
            # make a deque (first in last out)
            # place the tree in the deque by apending
            # acorss the length of the tree, add the left and right node of that level( in order in input)
            # add level counter when right and left are popped 
            # reurn level(should exit loop when tree values have been exauseted )


      
     

        
            
