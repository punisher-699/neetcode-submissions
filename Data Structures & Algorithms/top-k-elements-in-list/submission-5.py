class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ht = [0] * 10000

        # for i in nums:
        #     ht[nums[i]] += 1
        
        # ht.sort()

        # res = []

        # for i in range(k+1):
        #     res[i] = ht[i]

        ht = {}
        for num in nums:
            ht[num] = 1 + ht.get(num, 0)
        
        res = []
        for num, i in ht.items():
            res.append([i,num])
        res.sort()

        ans = []
        while len(ans) < k:
            ans.append(res.pop()[1])
        return ans
