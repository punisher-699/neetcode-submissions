class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height) 
        left = [0] * length
        right = [0] * length

        # left[0] , right[len(height) - 1] = 1000 , 1000
        # lmax , rmax = 0, 0
        # for i,h in enumerate(height):
            # if h > lmax:
            #     lmax = h
            # left[i] = h
            
            # if h > rmax:
            #     rmax = h
            # right[i] = h
        
        #lmax
        left[0] , right[length-1] = height[0] , height[length - 1]  
        for i in range(1, length):
            left[i] = max(height[i] , left[i - 1])
        for i in range(length - 2 , -1, -1):
            right[i] = max(height[i], right[i + 1])
        res = 0
        for i in range(0,length):
            res += min(left[i], right[i]) - height[i]
        return res
            

