# there can be two sorted arrays, left and right - separated by the pivot
# in [4,5,6,7,0,1,2]
# [4,5,6,7] is the left sorted array
# [0,1,2] is the right sorted array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # define left and right pointers
        left, right = 0, len(nums) - 1
        
        while left <= right: 
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            # left sorted array
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # right sorted array
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        # binary search complete and element not found
        return -1