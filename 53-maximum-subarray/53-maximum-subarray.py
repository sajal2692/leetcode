class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # check edge case of empty array
        if len(nums) < 0:
            return 0
        
        # initialize
        running_sum = 0
        max_sum = nums[0]
        
        # loop over array of nums
        for num in nums:
            # reset running_sum if the current running sum of array is below 0
            if running_sum < 0:
                running_sum = 0
            # add num to running_sum
            running_sum += num
            # update max_sum if needed
            max_sum = max(running_sum, max_sum)
        # end of loop, return the max_sum
        return max_sum
        