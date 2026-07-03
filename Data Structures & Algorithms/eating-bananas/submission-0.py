class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        piles.sort()

        if len(piles) == h:
            return piles[-1]
        
        #totalhours = sum(piles)

        #brute force
        res = float("inf")
        for pile in piles:
            time = 0
            for p in piles:
                if p <= pile:
                    time += 1
                else:
                    time += math.ceil(p / pile)
            if time <= h:
                res = min(res, pile)
        return res