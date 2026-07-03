class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        # speed = 1
        # while True:
        #     tt = 0
        #     for pile in piles:
        #         tt += math.ceil( pile / speed)
        #     if tt <= h:
        #         return speed
        #     speed += 1
        # return speed
        piles.sort()
        
        if len(piles) == h: return piles[-1]
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
            
