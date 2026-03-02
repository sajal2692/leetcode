class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_rows, num_cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == num_rows or c == num_cols or (r,c) in visited:
                return False
            if grid[r][c] == '0':
                return False

            visited.add((r, c))
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            return True

        island_count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if dfs(i, j):
                    island_count += 1

        return island_count
