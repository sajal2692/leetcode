class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        max_amount = 0
        while L < R:
            current_amount = (R-L) * min(height[L], height[R])
            max_amount = max(max_amount, current_amount)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return max_amount
