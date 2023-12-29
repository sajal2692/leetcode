class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer solution
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        amount = 0
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                amount += max(0, maxL -  height[l])
            else:
                r -= 1
                maxR = max(maxR, height[r])
                amount += max(0, maxR -  height[r])
        return amount  
        