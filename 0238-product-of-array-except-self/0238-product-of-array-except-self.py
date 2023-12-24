class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        prefix = [1] * len_nums
        postfix = [1] * len_nums
        output = []
        
        # calculate prefixes
        for i in range(len_nums):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1] * nums[i]
        
        # calculate postfixes
        for i in range(len_nums - 1, -1, -1):
            if i == len_nums - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i+1] * nums[i]

        # calculate output
        for i in range(len_nums):
            if i == 0:
                out = 1 * postfix[i + 1]
            elif i == len_nums -1:
                out = prefix[i - 1] * 1
            else:
                out = prefix[i-1] * postfix[i+1]
            output.append(out)

        return output