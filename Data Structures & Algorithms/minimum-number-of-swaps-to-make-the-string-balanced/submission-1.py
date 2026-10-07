class Solution:
    def isvalid(self, s):
        stack = []
        for ch in s:
            if ch == '[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0
    
    # def swapcheck(s, n):
    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s)):

    def minSwaps(self, s: str) -> int:
        if self.isvalid(s):
            return 0
        
        cur = 0
        maxv = 0

        for ch in s:
            if ch == '[':
                cur += 1
            else:
                cur -= 1   
            maxv = max(maxv, abs(cur))

        

        return (maxv + 1) // 2