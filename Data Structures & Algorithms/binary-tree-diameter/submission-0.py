# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
# can traverse nodes in a path visited, the output is the # of nodes visited in the longest path -1 
#The depth is everything to the right of the choosen node + everything to the left of the chosen node
# Using a helper function to make recursive calls, this function should update the global varible
# but then return the height of the node ( this is the max value of the right diameter or left subtree diameter of a certain node)

        maxdepth = 0
        def dfs(root):
            nonlocal maxdepth
            #use nonlocal word since it is modifying in the function ( recursivly calling this function means 
            # that we can initialize the pointer to 0 outside the function and it wond be updated to 0 every time the nonlocal varible in the secondary function is called 
            
            if root:
                rightd = (dfs(root.right))
                leftd = (dfs(root.left))
                maxdepth= max(maxdepth,rightd+leftd)
                return (1+max(leftd,rightd))
            else: 
                return 0 
        dfs(root)
        return maxdepth 

