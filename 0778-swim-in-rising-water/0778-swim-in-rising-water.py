class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        minHeap = [(grid[0][0], 0, 0)]
        
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            if r == R-1 and c == C-1:
                return t
            visited.add((r,c))
            for d in directions:
                dr, dc = d
                nr, nc = r+dr, c+dc
                if nr < 0 or nc < 0 or nr == R or nc == C or (nr, nc) in visited:
                    continue
                heapq.heappush(minHeap, (max(t, grid[nr][nc]), nr, nc))
            
