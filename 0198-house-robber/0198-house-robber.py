class Solution:
    def rob(self, nums: List[int]) -> int: 
        
        memo = {}

        def _rob(i):
            # base case
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0    
            memo[i] = max(_rob(i+1), nums[i] + _rob(i+2))
            return memo[i]

        return _rob(0)

        