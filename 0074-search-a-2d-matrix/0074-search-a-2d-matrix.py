class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bottom = 0, len(matrix) - 1
        
        # find the right row using binary search
        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        
        # pointers crossed, no element found
        if not top <= bottom:
            return False
        
        row = matrix[mid]
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > row[mid]:
                l = mid + 1
            elif target < row[mid]:
                r = mid - 1
            else:
                return True
        return False
            
            