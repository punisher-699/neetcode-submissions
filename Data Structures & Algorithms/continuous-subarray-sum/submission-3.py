class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # n = len(nums)
        # prefSum = [0] * n
        # c = 0
        # for i in range(n):
        #     c += nums[i]
        #     prefSum[i] = c
        
        # l = 0
        # for r in range(1, n):

        #     csum = 0
        #     for i in range(l, r):
        #         csum += nums[i]
        #     if csum % k == 0:
        #         return True
        n = len(nums)
        for i in range(0, n - 1):
            csum = nums[i]
            for j in range(i + 1, n):
                csum += nums[j]
                if csum % k == 0:
                    return True
        return False
            
