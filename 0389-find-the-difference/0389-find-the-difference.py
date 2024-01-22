from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = defaultdict(int)
        for c in s:
            count_s[c] += 1 
        for c in t:
            count_c = count_s.get(c, 0)
            if count_c == 0:
                return c
            else:
                count_s[c] -= 1
        