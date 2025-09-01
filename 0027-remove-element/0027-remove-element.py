class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l, r = 0,0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l