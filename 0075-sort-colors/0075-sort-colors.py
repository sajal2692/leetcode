class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count_colors = [0, 0, 0] # red, white, blue
        for n in nums:
            count_colors[n] += 1
        
        [2, 1, 4]
        
        i = 0
        # enumerate with index, count
        for color, count in enumerate(count_colors):
            for _ in range(count):
                nums[i] = color
                i += 1
        return nums