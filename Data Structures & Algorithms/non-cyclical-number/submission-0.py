class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)
            
            if n == 1:
                return True
        return False

    def sumOfSquares(self, n):

        r = 0
        while n:
            d = n % 10
            d = d ** 2
            r += d
            n //= 10
        return r
