from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
        

        inorder = [0] * numCourses

        for u in range(numCourses):
            for v in adj[u]:
                inorder[v] += 1
        
        q = deque()
        for u in range(numCourses):
            if inorder[u] == 0:
                q.append(u)
        
        res = 0
        while q:
            node = q.popleft()
            res += 1

            for v in adj[node]:
                inorder[v] -= 1

                if inorder[v] == 0:
                    q.append(v)
        return res == numCourses
