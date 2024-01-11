class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        l, r = 1, 1
        while r <= len(nums) - 1:
            if nums[r] == nums[r-1]:
                r += 1
            else:
                nums[l] = nums[r]
                l += 1
                r += 1
        return l