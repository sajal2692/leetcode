class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = {}

        def memo(i, j):
            if i >= m or j >= n:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if i == m - 1 and j == n - 1:
                return 1
            
            cache[(i,j)] = memo(i+1,j) + memo(i, j+1)
            return cache[(i,j)]
        
        return memo(0,0)