class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        cur = []
        res = []
        def dfs(cur, i, cursum):
            if cursum == target:
                res.append(cur.copy())
                return

            if i == len(nums) or cursum > target:
                #fahh 1
                return
            
            cur.append(nums[i])
            cursum += nums[i]

            
            
            dfs(cur, i , cursum)
            cur.pop()
            cursum -= nums[i]
            dfs(cur, i + 1, cursum)
        
        


        dfs(cur, 0, 0)
        return res

