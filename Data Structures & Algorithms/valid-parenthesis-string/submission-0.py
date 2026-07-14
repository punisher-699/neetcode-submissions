class Solution:
    def checkValidString(self, s: str) -> bool:
        
        starcount = 0
        stack = []
        s = s.replace(' ','')
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == '*':
                starcount += 1
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
        if len(stack) <= starcount:
            return True
        return False

    