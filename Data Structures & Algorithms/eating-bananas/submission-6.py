class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = l + (r - l) // 2
            tt = 0
            for pile in piles:
                tt += math.ceil(pile / m)
            if tt <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
            
