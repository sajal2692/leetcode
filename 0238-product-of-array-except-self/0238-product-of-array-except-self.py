class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        output = [1] * len(nums)
        
        # forward pass
        prefix = 1
        for i in range(len_nums):
            output[i] = prefix
            prefix *= nums[i]
            
        #backward pass
        postfix = 1
        for i in range(len_nums - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output