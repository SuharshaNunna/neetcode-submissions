# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # tree traversal, return count of longest path, 
        # can keep track of max depth within regular tree traversal
        # max depth of left child and right child = max depth of root +1  
        if root is None:
            return 0
        else: 
            return (max(self.maxDepth(root.left), self.maxDepth(root.right))+1)
        