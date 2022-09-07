class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        for i in range(len(nums)):
            if i == 0:
                running_sum.append(nums[i])
                continue
            running_sum.append(nums[i] + running_sum[i-1])
        return running_sum
            