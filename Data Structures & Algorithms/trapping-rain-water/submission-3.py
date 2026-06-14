class Solution:
    def trap(self, height: List[int]) -> int:
        
        lmax , rmax = height[0] , height[len(height)-1]
        res = 0
        left , right = 1 , len(height)-2

        while left <= right:
            if lmax < rmax:
                lmax = max(lmax, height[left])
                res += lmax - height[left]
                left += 1
            else:
                rmax = max(rmax , height[right])
                res += rmax - height[right]
                right -= 1
        return res
