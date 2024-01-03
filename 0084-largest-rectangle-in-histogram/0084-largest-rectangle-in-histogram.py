class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # pair (index, height)
        
        for current_index, current_height in enumerate(heights):
            start = current_index
            while stack and stack[-1][1] > current_height:
                prev_index, prev_height = stack.pop()
                current_rectangle_area = prev_height * (current_index - prev_index)
                max_area = max(max_area, current_rectangle_area)
                start = prev_index
            stack.append((start, current_height))
            
        for index, height in stack:
            current_rectangle_area = height * (len(heights) - index)
            max_area = max(max_area, current_rectangle_area)
        
        return max_area
            