class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for n in nums_set:
            if n-1 in nums_set:
                continue
            step = 0
            while n + step in nums_set:
                step += 1
                max_length = max(max_length, step)
        return max_length

            
