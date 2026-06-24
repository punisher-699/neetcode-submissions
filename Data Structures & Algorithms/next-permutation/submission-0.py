class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        pi = -1

        for i in range(len(nums) - 1 , 0 , -1):
            if nums[i] > nums[i - 1]:
                pivot = nums[i - 1]
                pi = i - 1
                break
        else:
            nums.reverse()
            return

        temp = float("infinity")
        swpi = -1
        for i in range(pi + 1 , len(nums)):
            if nums[i] > pivot and nums[i] <= temp:
                temp = nums[i]
                swpi = i

        temp = nums[pi]
        nums[pi] = nums[swpi]
        nums[swpi] = temp
        
        st = pi + 1
        end = len(nums) - 1

        while st < end:
            temp = nums[st]
            nums[st] = nums[end]
            nums[end] = temp
            st += 1
            end -= 1
