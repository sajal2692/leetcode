class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        num_rows, num_cols = len(grid), len(grid[0])
        max_area = -float("inf")
        visited = set()

        def dfs(r, c):

            if r < 0 or c < 0 or r == num_rows or c == num_cols:
                return 0
            if (r,c) in visited:
                return 0
            if grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            area = 1

            area += dfs(r-1, c)
            area += dfs(r+1, c)
            area += dfs(r, c-1)
            area += dfs(r, c+1)

            return area
        
        for r in range(num_rows):
            for c in range(num_cols):
                max_area = max(max_area, dfs(r,c))
        
        return max_area
            

        