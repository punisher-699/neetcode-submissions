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
        
        ump = 0
        stack = []

        for ch in s:
            if ch == '[':
                stack.append(ch)
            else:
                if not stack:
                    ump += 1
                else:
                    stack.pop()
        ump += (len(stack) // 2)

        return (ump + 1) // 2