class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        cur = []
        res = []
        def dfs(cur, i, cursum):
            if cursum == target:
                res.append(cur.copy())
                return

            if i == len(candidates) or cursum > target:
                #fahh 1
                return
            
            cur.append(candidates[i])
            cursum += candidates[i]

            
            
            dfs(cur, i + 1, cursum)
            cur.pop()
            cursum -= candidates[i]
            dfs(cur, i + 1, cursum)
        
        


        dfs(cur, 0, 0)
        return res

