class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ns = set(numbers)

        for num in numbers:
            if target - num in ns :
                return [numbers.index(num)+1,numbers.index(target - num)+1]
        return []
        