class Solution:
    def trap(self, height: List[int]) -> int:
        

        stack = []
        res = 0
        for i, h in enumerate(height): 
            while stack and h > stack[-1][1]:
                tw, th = stack.pop()
                if stack:
                    lefti, lefth = stack[-1]
                    fh = min(lefth, h) - th
                    fw = i - lefti - 1
                    res += fh * fw
            stack.append([i, h])

        return res
