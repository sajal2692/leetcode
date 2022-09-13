from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_2_count = defaultdict(int)
        for char in s:
            char_2_count[char] += 1
        for i in range(len(s)):
            if char_2_count[s[i]] == 1:
                return i
        return -1