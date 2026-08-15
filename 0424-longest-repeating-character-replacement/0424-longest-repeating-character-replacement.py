class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        L = 0
        count = {}
        max_count = 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            max_count = max(max_count, count[s[R]])
            while  (R - L + 1) - max_count > k:
                count[s[L]] -= 1
                L += 1

            result = max(result,  R - L + 1) 
        
        return result