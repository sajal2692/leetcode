class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l,r = 1,1
        while r < n:
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l = l + 1
            r = r + 1
        return l