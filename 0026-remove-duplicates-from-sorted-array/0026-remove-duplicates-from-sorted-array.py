class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 1, 1
        while R < len(nums):
            if not nums[R] == nums[R-1]:
                nums[L] = nums[R]
                L += 1
            R += 1
        return L