class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        res = 0
        cnt = defaultdict(int)

        for num in nums:
            res += cnt[num] 
            cnt[num] += 1
        return res