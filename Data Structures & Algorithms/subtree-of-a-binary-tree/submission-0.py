# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#if the node of root is == to subroots node then go into checking id the next elements ( children are all the same)
# automatic false is if subroot is bigger than root 
# traverse root making sure to check if the curr node is = to subroots node
# recursive approach 
 
 # returns true when  subroot and root are finished traversing and == eachother 
        if not subRoot :
            return True 
        if not root:
            return False 
# check of same subtree
        if self.sameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root,subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val== subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right,subRoot.right))
        else:
            return False
        