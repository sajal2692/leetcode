class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        counts = {n:0 for n in nums}
        for n in nums:
            counts[n] += 1
        
        def dfs():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
            for n in counts:
                if counts[n] > 0:
                    perm.append(n)
                    counts[n] -= 1
                    dfs()
                    perm.pop()
                    counts[n] += 1
        dfs()
        return result
