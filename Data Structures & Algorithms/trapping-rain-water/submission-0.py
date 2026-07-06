class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxleft = height[left]
        maxright = height[right]
        res = 0

        while left < right :
            if height[left] < height[right]:
                left += 1
                maxleft = max(maxleft,height[left])
                res += maxleft-height[left]
            else :
                right -= 1
                maxright = max(maxright,height[right])
                res += maxright - height[right]

        return res

    
            

        
        
        