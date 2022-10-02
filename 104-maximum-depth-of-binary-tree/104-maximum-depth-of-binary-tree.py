# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursion base cas
        if not root:
            return 0
        # return 1 (depth of current level) + max of the depths of the sub-trees at left and right nodes
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))