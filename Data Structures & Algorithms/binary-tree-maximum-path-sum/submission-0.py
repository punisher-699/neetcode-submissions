# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = cur = root.val

        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            lsum = dfs(node.left)
            rsum = dfs(node.right)

            lsum = max(0, lsum)
            rsum = max(0, rsum)

            #with split
            res = max(res, node.val + lsum + rsum)     
            #no split
            #return max(0, lsum, rsum) + node.val
            return node.val + max(lsum, rsum)
        
        dfs(root)
        return res
