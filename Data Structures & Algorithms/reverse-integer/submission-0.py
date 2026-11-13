class Solution:
    def reverse(self, x: int) -> int:
        # neg = False
        # if x < 0:
        #     neg = True

        MAX = 2 ** 31 - 1
        MIN = -2 ** 31
        res = 0
        temp = x
        while temp:
            d = int(math.fmod(temp, 10))
            temp = int(temp / 10)

            if (res > MAX // 10 or 
                res == MAX // 10 and d >= MAX % 10):
                return 0
            if (res < MIN // 10 or
                res == MIN // 10 and d <= MIN % 10 ):
                return 0
            res = res * 10 + d
            
        #if res > (2 ** 31 - 1) or res < (-2 ** 31): return 0
        #return -res if neg else res
        return res
