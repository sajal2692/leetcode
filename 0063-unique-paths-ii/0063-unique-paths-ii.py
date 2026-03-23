class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])

        # top down dp
        # cache = {}

        # def dfs(row, col):
        #     if row >= num_rows or col >= num_cols:
        #         return 0
        #     if obstacleGrid[row][col] == 1:
        #         return 0
        #     if (row,col) in cache: return cache[(row,col)]
        #     if row == num_rows - 1 and col == num_cols - 1:
        #         return 1
            
        #     cache[(row,col)] =  dfs(row+1, col) + dfs(row, col+1)
        #     return cache[(row,col)]
        
        # return dfs(0,0)

        # bottom up dp
        
        obstacleGrid[-1][-1] = 1 if obstacleGrid[-1][-1] == 0 else 0

        for r in range(num_rows - 1, -1, -1):
            for c in range(num_cols -1, -1, -1):
                if r == num_rows - 1 and c == num_cols - 1:
                    continue
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    below = obstacleGrid[r+1][c] if r+1 < num_rows else 0
                    right = obstacleGrid[r][c+1] if c+1 < num_cols else 0
                    obstacleGrid[r][c] = below + right
        
        return obstacleGrid[0][0]
                
            

