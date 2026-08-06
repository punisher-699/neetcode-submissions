class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ht = {}

        for num in nums:
            ht[num] = 1 + ht.get(num, 0)
        
        heap = []
        for num in ht.keys():
            heapq.heappush(heap, [-ht[num], num])
        
        #res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        res = [heapq.heappop(heap)[1] for _ in range(k)]
        return res
            
        