class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        res = [0] * len(temperatures)
        stack = [] #this will be index : temp pair

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                stindex , sttemp = stack.pop()
                res[stindex] = (i - stindex)
            stack.append([i, temp])
        return res

