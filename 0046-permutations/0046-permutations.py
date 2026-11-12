class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perms = [[]]
        for n in nums:
            next_perm = []
            for perm in perms:
                for j in range(len(perm) + 1):
                    p = perm.copy()
                    p.insert(j, n)
                    next_perm.append(p)
            perms = next_perm
        return perms