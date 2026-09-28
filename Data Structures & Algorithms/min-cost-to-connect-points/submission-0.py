import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        adj = {i : [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                distance = abs(x2 - x1) + abs(y2 - y1)

                adj[i].append([distance, j])
                adj[j].append([distance, i])
        
        res = 0
        visited = set()
        heap = [[0, 0]]
        while len(visited) < n:

            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            
            res += cost
            visited.add(node)

            for c, nb in adj[node]:
                if nb not in visited:
                    heapq.heappush(heap, (c, nb))
        
        return res

            