class Solution(object):
    
    def searchRow(self, row, target):
        l = 0
        r = len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) -1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][left] > target:
                bottom = mid - 1
            elif matrix[mid][right] < target:
                top = mid + 1
            else:
                return self.searchRow(matrix[mid], target)
        return False
