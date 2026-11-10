class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        comb = []

        def helper(i):
            if len(comb) == k:
                res.append(comb.copy())
                return
            if i > n:
                return
            
            for j in range(i, n+1):
                comb.append(j)
                helper(j+1)
                comb.pop()
        
        helper(1)
        return res


