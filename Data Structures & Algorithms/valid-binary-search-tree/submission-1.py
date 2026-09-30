# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #dfs?
        # cant just check neighbors becuase comparisson might be true but the actuall whole tree may not be valid
        # keep track of intervals that te pair van be valid 
        # moving left means update right boundry and moving right means updating left boundry 
        def valid(node,left,right):
            if not node: 
                return True 
            if not (node.val <right and node.val>left):
                return False
            return valid(node.left,left,node.val) and valid(node.right,node.val,right)
        return valid(root,float("-inf"),float("inf"))
        