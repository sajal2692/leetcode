class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result, curset  = [], []

        def helper(i):
            if i >= len(nums):
                result.append(curset.copy())
                return
            curset.append(nums[i])
            helper(i+1)
            curset.pop()

            while i+1<len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            helper(i+1)
        
        helper(0)
        return result 