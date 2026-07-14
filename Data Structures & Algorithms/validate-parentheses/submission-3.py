class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        matcher = { ')' : '(', ']' : '[', '}' : '{'}

        for c in s:
            if c in matcher:
                if stack and stack[-1] == matcher[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
                