class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * 2 * n
        for i in range(n):
            ans[i] = ans[i+n] = nums[i]
        return ans
        