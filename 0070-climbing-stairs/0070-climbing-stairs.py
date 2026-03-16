class Solution:
    def climbStairs(self, n: int) -> int:
        
        # top down dp / memoization
        # def climb(n, cache):
        #     if n in cache:
        #         return cache[n]
        #     if n == 0:
        #         return 1
        #     if n < 0:
        #         return 0
            
        #     cache[n] = climb(n-1, cache) + climb(n-2, cache)
        #     return cache[n]
    
        # return climb(n, {})

        if n == 0:
            return 1
        if n < 0:
            return 0
        
        dp = [1, 1] # init with ways to climb for 0 and 1

        i = 2
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = tmp
            i += 1
        return dp[1]