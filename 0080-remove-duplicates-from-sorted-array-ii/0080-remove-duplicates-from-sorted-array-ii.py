class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        L, R = 2, 2
        while R < len(nums):
            if nums[R] != nums[L-2]:
                nums[L] = nums[R]
                L += 1
            R += 1
        return L
            