class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ht = {}
        for num in nums:
            ht[num] = 1 + ht.get(num, 0)
        
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in ht.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res