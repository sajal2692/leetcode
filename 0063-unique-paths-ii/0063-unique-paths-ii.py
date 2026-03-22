class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])
        cache = {}

        def dfs(row, col):
            if row >= num_rows or col >= num_cols:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if (row,col) in cache: return cache[(row,col)]
            if row == num_rows - 1 and col == num_cols - 1:
                return 1
            
            cache[(row,col)] =  dfs(row+1, col) + dfs(row, col+1)
            return cache[(row,col)]
        
        return dfs(0,0)
