class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # jr, dest = 0, len(nums) - 1
        # j = 0
        
        # while j < dest:
        #     if nums[j] == 0:
        #         return False
        #     jr += nums[j]
        #     j = jr
        
        # return jr >= dest

        dest = len(nums) - 1
        for i in range(len(nums) - 2, - 1, -1):
            if nums[i] + i >= dest:
                dest = i
        return dest == 0

