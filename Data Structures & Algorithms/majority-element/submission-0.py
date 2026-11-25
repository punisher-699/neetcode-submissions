class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        thr = n // 2

        ht = {}

        for num in nums:
            ht[num] = ht.get(num, 0) + 1
            if ht[num] > thr:
                return num
        