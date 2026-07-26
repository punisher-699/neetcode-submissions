class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        heap = []

        for x, y in points:
            d = x * x + y * y
            heapq.heappush(heap, [d, [x, y]])
        
        return [heapq.heappop(heap)[1] for i in range(k)]

