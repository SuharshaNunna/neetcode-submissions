# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # compare root of subtree with root of og tree , if it doesnt match keep traversing , if it does match,incirment subroot (another call) see if that matches , keep incremtinging if it matches or not, if it doesnt match at one point reset subroot root and keep traversing root untill every node is accessed 
        def sameTree(root,subRoot):
            if root is None and subRoot is None:
                return True 
            if root and subRoot and root.val== subRoot.val:
                return (sameTree(root.left,subRoot.left) and sameTree(root.right,subRoot.right))
            else:
                return False
        if subRoot is None:
            return True 
        elif root is None:
            return False  
        if sameTree(root,subRoot):
                return True
        return (self.isSubtree(root.left,subRoot)or self.isSubtree(root.right,subRoot))

        

        