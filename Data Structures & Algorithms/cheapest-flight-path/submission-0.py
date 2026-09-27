import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        
        adjlist = [[] for _ in range(n)]

        for u, v, pr in flights:
            adjlist[u].append((v, pr))
        
    
        heap = []
        heapq.heappush(heap, (0, src, 0))

        while heap:

            pr, node, stops = heapq.heappop(heap)
            if stops > k + 1:
                continue
            if node == dst:
                return pr
            
            for nb, p in adjlist[node]:
                
                heapq.heappush(heap, (pr + p, nb, stops + 1))
        
        return -1

