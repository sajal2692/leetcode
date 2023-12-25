class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_seq = 0
        for num in nums:
            if num - 1 in set_nums:
                continue
            current_seq = 1
            while num + current_seq in set_nums:
                current_seq += 1
            longest_seq = max(longest_seq, current_seq)
        return longest_seq
            
            
        