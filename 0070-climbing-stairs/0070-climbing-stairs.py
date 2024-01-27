class Solution:
    def climbStairs(self, n: int) -> int:
        
        n_2_res = {}
        
        def climb(n):
            # base case
            if n <= 1:
                return 1

            if n in n_2_res:
                return n_2_res[n]

            # recursive case with memoization
            n_2_res[n] = climb(n-1) + climb(n-2)
            
            return n_2_res[n]
        
        return climb(n)
        