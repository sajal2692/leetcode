class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # memoization approach (top down dp)
        # cache = {}

        # def memo(i, j):
        #     if i >= m or j >= n:
        #         return 0
        #     if (i,j) in cache:
        #         return cache[(i,j)]
        #     if i == m - 1 and j == n - 1:
        #         return 1
            
        #     cache[(i,j)] = memo(i+1,j) + memo(i, j+1)
        #     return cache[(i,j)]
        
        # return memo(0,0)

        # bottom up dp

        prev_row = [0] * n

        for i in range(m - 1, -1, -1):
            cur_row = [0] * n
            cur_row[n-1] = 1
            for j in range(n - 2, -1, -1):
                cur_row[j] = cur_row[j+1] + prev_row[j]
            prev_row = cur_row
        return prev_row[0]