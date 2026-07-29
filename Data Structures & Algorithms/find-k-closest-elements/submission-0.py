class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        heap = []

        for num in arr:
            dist = abs(num - x)
            heapq.heappush(heap, (dist, num))
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return sorted(ans)