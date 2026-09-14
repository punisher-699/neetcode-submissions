from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjlist = [[] for _ in range(numCourses)]
        for v, u in prerequisites:
            adjlist[u].append(v)

        indegree = [0] * numCourses
        for u in range(numCourses):
            for v in adjlist[u]:
                indegree[v] += 1

        q = deque()  
        for u in range(numCourses):
            if indegree[u] == 0:
                q.append(u)
        
        res = []
        count = 0
        while q:
            node = q.popleft()
            res.append(node)
            count += 1
            for nb in adjlist[node]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)
        return res if count == numCourses else []