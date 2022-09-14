class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) < 0:
            return 0
        
        current_sum = 0
        max_sum = nums[0]
        
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_sum = max(current_sum, max_sum)
        return max_sum
        