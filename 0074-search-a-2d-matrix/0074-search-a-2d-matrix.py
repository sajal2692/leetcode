class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(array: List[int]) -> bool:            
            l, r = 0, len(array) - 1
            while l <= r:
                m = (l + r) // 2
                if array[m] == target:
                    return True
                elif array[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False
        
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            m = (top + bottom) // 2
            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bottom = m - 1
            else:
                break
        # run binary search on the middle row (the one that was found)
        return binarySearch(matrix[m])
                    