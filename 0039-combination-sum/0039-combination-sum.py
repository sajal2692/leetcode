class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def dfs(i):
            # perform dfs with backtracking
            # base case: overshoot
            if sum(combination) > target or i >= len(candidates):
                return
            # base case: found working combination    
            if sum(combination) == target:
                res.append(combination.copy())
                return
            # add candindate to combination
            combination.append(candidates[i])
            # try adding with additional copy of same candidate
            dfs(i)
            # try adding with next number after removing current copy
            combination.pop()
            dfs(i+1)

        dfs(0)
        return res 