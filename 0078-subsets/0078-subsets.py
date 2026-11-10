class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result, curset = [], []

        def helper(i):

            if i >= len(nums):
                result.append(curset.copy())
                return
            
            curset.append(nums[i])
            helper(i+1)
            curset.pop()
            helper(i+1)
        
        helper(0)
        return result
            