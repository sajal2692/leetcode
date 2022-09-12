class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize a result array of the same length
        result = [1] * len(nums)
        
        # we traverse the result array twice, 1 forward pass + 1 backward pass
        # forward pass
        prefix = 1 # keep track of the cumulative product of prefixes
        for i in range(len(result)):
            # multiply current result num in result by current prefix
            result[i] *= prefix
            # multiply prefix by current num
            prefix *= nums[i]
        # backward pass # keep track of cumulative product of postfixes
        postfix = 1
        for i in reversed(range(len(result))):
            result[i] *= postfix
            postfix *= nums[i]
            
        return result