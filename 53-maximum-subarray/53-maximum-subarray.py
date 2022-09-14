class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        max_sum = - float("inf")
        window_sum = 0
        while r < len(nums):
            window_sum += nums[r]
            max_sum = max(max_sum, window_sum)
            if window_sum < 0:
                l = r + 1
                r = l
                window_sum = 0
            else:
                r += 1
        return max_sum
