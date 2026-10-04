class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        q = deque()

        for i, t in enumerate(tickets):
            q.append([i, t])
        
        res = 1
        while q:
            q[0][1] -= 1
            if q[0][1] == 0:
                if q[0][0] == k:
                    break
                
                else:
                    q.popleft()
            else:
                q.append(q.popleft())
            
            res += 1
        return res