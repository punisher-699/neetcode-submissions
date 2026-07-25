# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node.left and not node.right:
                return True

            if node.left.val > node.val or node.val > node.right.val:
                return False
            return dfs(node.left) and dfs(node.right)
        
        return dfs(root)
