class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        L = 0
        sum = 0

        for R in range(len(nums)):
            sum += nums[R]
            while sum >= target:
                length = min(length, R - L + 1)
                sum -= nums[L]
                L += 1
        return 0 if length == float("inf") else length
            
        # [2, 3, 1, 2, 4, 3]
        #              L. R
        # sum = 6
        # length = 2
                