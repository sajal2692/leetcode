class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_2_index = {}
        for i in range(len(nums)):
            value = nums[i]
            difference = target - value
            if difference in value_2_index:
                return [i, value_2_index[difference]]
            value_2_index[value] = i