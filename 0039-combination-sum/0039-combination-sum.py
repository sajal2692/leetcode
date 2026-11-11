class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        curcomb = []
        results = []

        def dfs(i):
            if sum(curcomb) == target:
                results.append(curcomb.copy())
                return
            if i == len(candidates) or sum(curcomb) > target:
                return
            
            curcomb.append(candidates[i])
            dfs(i)
            curcomb.pop()
            dfs(i+1)
        
        dfs(0)
        return results