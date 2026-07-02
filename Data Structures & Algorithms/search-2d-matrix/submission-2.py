class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = -1
        ol, orr = 0, len(matrix) - 1

        while ol <= orr:
            mid = (orr - ol)//2 + ol

            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            if target < matrix[mid][0]:
                orr = mid - 1
            elif target > matrix[mid][-1]:
                ol = mid + 1
            else:
                row = mid
                break
                
        if row == -1 : return False    
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False