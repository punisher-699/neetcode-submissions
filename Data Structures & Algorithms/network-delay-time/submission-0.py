import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        dist = [float('inf')] * (n + 1)
        adjlist = [[] for _ in range(n + 1)]

        for u, v, w in times:
            adjlist[u].append((v, w))
        
        dist[k] = 0
        heap = []

        heapq.heappush(heap, (0, k))

        while heap:

            dis, node = heapq.heappop(heap)
            if dis > dist[node]:
                continue
            
            for nb, d in adjlist[node]:
                if d + dis < dist[nb]:
                    dist[nb] = d + dis
                    heapq.heappush(heap, (dist[nb], nb))
        res = max(dist[1: ])
        return -1 if res == float('inf') else res