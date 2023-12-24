class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        prefix = [1] * len_nums
        postfix = [1] * len_nums
        output = []
        # calculate prefixes
        for i in range(len_nums):
            if i == 0:
                continue
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # calculate postfixes
        for i in range(len_nums - 1, -1, -1):
            print(i)
            if i == len_nums - 1:
                continue
            postfix[i] = postfix[i+1] * nums[i+1]

        for i in range(len_nums):
          output.append(prefix[i] * postfix[i])

        return output