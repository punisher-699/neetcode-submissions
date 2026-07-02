class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        ol, orr = 0, len(matrix) - 1

        while ol <= orr:
            mid = (orr - ol)//2 + ol

            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            if matrix[mid][0] < target and matrix[mid][-1] < target:
                ol = mid + 1
            else:
                orr = mid - 1
            
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if matrix[ol][mid] == target:
                return True
            if matrix[ol][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False