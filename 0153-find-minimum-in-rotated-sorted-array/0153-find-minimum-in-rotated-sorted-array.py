class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [4,5,6,7,0,1,2] = 0
        l, r = 0, len(nums) - 1
        minElement = float("inf")
        while l <= r:
            if nums[l] <= nums[r]:
                return min(minElement, nums[l])
            else:
                mid = (l + r) // 2
                minElement = min(minElement, nums[mid])
                if nums[mid] >= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return minElement
        
        # [3, 4, 5, 1, 2]
        
        # 
            
            
            
        
        
        