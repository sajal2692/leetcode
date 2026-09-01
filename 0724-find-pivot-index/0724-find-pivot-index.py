class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            curr = nums[i]
            if total - left_sum - curr == left_sum:
                return i
            left_sum += curr
        return -1