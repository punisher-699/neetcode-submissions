class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pi = -1

        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pi = i - 1
                break

        else:
            nums.reverse()
            return
        
        nextg = float('inf')
        nextgi = -1

        pv = nums[pi]
        for i in range(pi + 1, n):
            if nums[i] > pv and nums[i] <= nextg:
                nextg = nums[i]
                nextgi = i
                
        nums[pi], nums[nextgi] = nextg, pv
        
        st, end = pi + 1, n - 1
        while st < end:
            nums[st], nums[end] = nums[end], nums[st]
            st += 1
            end -= 1
        



