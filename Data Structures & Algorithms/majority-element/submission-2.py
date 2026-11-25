class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        while True:
            cand = random.choice(nums)
            if nums.count(cand) > n // 2:
                return cand