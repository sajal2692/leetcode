class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_nums = set()
        for num in nums:
            if num in seen_nums:
                return True
            seen_nums.add(num)
        return False
        
        