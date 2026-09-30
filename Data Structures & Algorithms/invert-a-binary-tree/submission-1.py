# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # invert= left child and right child switch positions
        # start from top and move down; left child val = right, right value = left 
        # swap pointers 
        if not root:
            return None
        root.left,root.right = root.right,root.left 
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        