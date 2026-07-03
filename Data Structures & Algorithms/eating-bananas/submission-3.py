class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        speed = 1
        while True:
            tt = 0
            for pile in piles:
                tt += math.ceil( pile / speed)
            if tt <= h:
                return speed
            speed += 1
        return speed
        