class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        heap = [-num for num in nums]
        heapq.heapify(heap)

        return -heap[k - 1]