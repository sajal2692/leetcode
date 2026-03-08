class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        num_rows, num_cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        minutes = 0

        neighbours = [
            (-1,0), (1,0), (0,1), (0,-1)
        ]

        # seed_queue
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 2:
                    queue.append((r,c))

        while queue:
            did_rot = False
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in neighbours:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < num_rows and 0 <= nc < num_cols and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        did_rot = True
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            if did_rot:
                minutes += 1
        
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    return -1
        return minutes

        
                    


            
        