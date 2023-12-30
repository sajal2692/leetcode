class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_length = 0
        len_s = len(s)
        for i in range(len_s):
            if s[i] != " ":
                if s[i-1] == " ":
                    last_length = 1
                else:
                    last_length += 1
        return last_length
                