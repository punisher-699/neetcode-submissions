class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        sp = [[p,s] for p,s in zip(position,speed)]
        sp.sort(reverse = True)
        stack = []

        for i in range(len(sp)):
            stack.append((target - sp[i][0])/ sp[i][1])
            if len(stack) >=2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)