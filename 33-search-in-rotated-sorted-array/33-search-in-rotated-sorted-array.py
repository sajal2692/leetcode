# there can be two sorted arrays, left and right - separated by the pivot
# in [4,5,6,7,0,1,2]
# [4,5,6,7] is the left sorted array
# [0,1,2] is the right sorted array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # define left and right pointers:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # target found in the middle
            if target == nums[mid]:
                return mid
            
            # left sorted array
            if nums[left] <= nums[mid]:
                # within left sorted array, target > mid element or smaller than left edge
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # right sorted array
            else:
                # within right sorted array, target < mid element or greater than right edge
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        # target not found
        return -1