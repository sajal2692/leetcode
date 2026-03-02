class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def findIslands(grid, r, c, visited, island, num_rows, num_cols):
            # check out of bounds
            if r < 0 or c < 0 or r == num_rows or c == num_cols or (r,c) in visited:
                return 0
            if grid[r][c] == '0':
                return 0
            
            visited.add((r,c))
            island.add((r,c))

            findIslands(grid, r-1, c, visited, island, num_rows, num_cols)
            findIslands(grid, r+1, c, visited, island, num_rows, num_cols)
            findIslands(grid, r, c-1, visited, island, num_rows, num_cols)
            findIslands(grid, r, c+1, visited, island, num_rows, num_cols)

            if island:
                return 1

        island_count = 0
        visited = set()
        num_rows, num_cols = len(grid), len(grid[0])

        for i in range(num_rows):
            for j in range(num_cols):
                island_count += findIslands(grid, i, j, visited, set(), num_rows, num_cols)
        
        return island_count


