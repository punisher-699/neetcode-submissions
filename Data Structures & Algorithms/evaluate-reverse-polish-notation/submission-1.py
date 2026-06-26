class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for tok in tokens:
            if tok not in "+-*/":
                stack.append(int(tok))
            else:
                r = 0
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if tok == '+':
                    r = val2 + val1
                elif tok == '-':
                    r = val2 - val1
                elif tok == '*':
                    r = val2 * val1
                elif tok == '/':
                    r = int(val2 / val1)
                stack.append(r)
        return stack.pop()