class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        res.append(1)
        for i in range(1,len(nums)):
            t = res[i-1] * nums[i-1]
            res.append(t)
        temp = 1
        for i in range(len(nums) - 1 , -1, -1):
            res[i] *= temp
            temp *= nums[i]
        return res