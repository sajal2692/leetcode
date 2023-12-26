class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        print(nums)
        len_nums = len(nums)
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i + 1, len_nums - 1
            while l < r:
                if (l > i + 1 and nums[l] == nums[l-1]) and (r < len_nums - 1and nums[r] == nums[r+1]):
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + num == 0:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + num < 0:
                    l += 1
                elif nums[l] + nums[r] + num > 0:
                    r -= 1
        return result