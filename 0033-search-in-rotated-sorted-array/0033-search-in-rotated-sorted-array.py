class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # example: [4, 5, 6, 7, 0, 1, 2]
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # if mid in the left sorted array i.e. [4, 5, 6, 7]
            if nums[l] <= nums[mid]:
                # anything greater than mid will be on the right
                # if the target is smaller than nums[l], it can only be on the right
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # if mid in the right sorted array i.e. [0, 1, 2]
            else:
                # anything smaller than mid will always be on the left
                # if the target is greater than nums[r], it can only be on the left
                if nums[mid] > target or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1