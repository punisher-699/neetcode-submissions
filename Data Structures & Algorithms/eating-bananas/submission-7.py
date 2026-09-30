class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, high = 1, max(piles)
        res = 0
        while low <= high:

            mid = (low + high) // 2
            c_time = 0
            for b in piles:
                c_time += math.ceil(b / mid)
            
            if c_time > h:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        
        return res
            
            