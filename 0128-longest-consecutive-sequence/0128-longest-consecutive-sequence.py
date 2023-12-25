class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_seq_length = 0
        for num in nums:
            current_seq_length = 0
            if num - 1 in set_nums:
                continue
            current_num = num
            current_seq_length += 1
            current_num += 1
            while current_num in set_nums:
                current_seq_length += 1
                current_num += 1
            longest_seq_length = max(current_seq_length, longest_seq_length)
        return longest_seq_length
                
                
            
            
        