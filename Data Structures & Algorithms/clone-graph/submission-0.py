"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        ht = {}

        def dfs(node):

            if node in ht:
                return ht[node]

            temp = Node(node.val)
            ht[node] = temp
            for nb in node.neighbors:
                temp.neighbors.append(dfs(nb))
            return temp
        
        return dfs(node) if node else None

        