class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(n, cache):
            if n in cache:
                return cache[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            cache[n] = climb(n-1, cache) + climb(n-2, cache)
            return cache[n]
    
        return climb(n, {})