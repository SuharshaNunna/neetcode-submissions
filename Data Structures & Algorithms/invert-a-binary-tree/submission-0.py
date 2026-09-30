# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # root stays the same
        # all left values are flipped to right (vise versa)
        # go through tree until reaching the end 
        #using recursive not iterative approach ( dont need to store it all in a loop)
        # swap the children of each child
        if not root:
            return None

        temp=root.right
        root.right =root.left 
        root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        