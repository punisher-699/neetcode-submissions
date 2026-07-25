class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            #if (mid - 1 < 0 or nums[mid - 1] != nums[mid]) and (mid + 1 > len(nums) - 1 or nums[mid] != nums[mid + 1]):
            if ((mid == 0 or nums[mid - 1] != nums[mid]) and
                (mid == len(nums) - 1 or nums[mid + 1] != nums[mid])):
                return nums[mid] 

            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 1
                elif nums[mid] == nums[mid - 1]:
                    right = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


