class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[num_rows-1][num_cols-1] == 1:
            return -1


        visited = set()
        queue = deque()
        visited.add((0,0))
        queue.append((0,0))
        
        length = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                # base case, reached destination
                if r == num_rows - 1 and c == num_cols - 1:
                    return length

                neighbours = [
                    (0,-1), (0,1), (-1,0), (1,0),
                    (-1,-1), (-1,1), (1,1), (1,-1)
                ]

                for dr, dc in neighbours:
                    new_r, new_c = r + dr, c + dc

                    if new_r < 0 or new_c < 0 \
                    or (new_r, new_c) in visited \
                    or new_r == num_rows \
                    or new_c == num_cols \
                    or grid[new_r][new_c] == 1:
                        continue
                    
                    queue.append((new_r, new_c))
                    visited.add((new_r, new_c))
                
            length += 1
        
        return -1

