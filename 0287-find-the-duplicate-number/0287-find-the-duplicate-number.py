class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        slow_2 = nums[0]
        while slow_2 != slow:
            slow = nums[slow]
            slow_2 = nums[slow_2]
        
        return slow
        