class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        prefix_right = self.prefix[right]
        prefix_left = self.prefix[left - 1] if left > 0 else 0
        return prefix_right - prefix_left



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)