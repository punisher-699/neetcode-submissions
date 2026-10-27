# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return -1
            l = dfs(node.left)
            if l == -2:
                return -2

            r = dfs(node.right)
            if r == -2:
                return -2

            if abs(l - r) > 1:
                return -2
            return 1 + max(l, r)
        return dfs(root) != -2