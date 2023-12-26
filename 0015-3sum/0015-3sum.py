class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # sort so that can use two pointer approach
        nums.sort()
        len_nums = len(nums)
        for i, n in enumerate(nums):
            # if the starting number is the same as the previous one in the list, continue
            if i > 0 and n == nums[i-1]:
                continue
            # set up two pointers
            l, r = i + 1, len_nums - 1
            while l < r:
                three_sum = n + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    result.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # if the left pointer is the same as the previous left pointer, move it ahead
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return result