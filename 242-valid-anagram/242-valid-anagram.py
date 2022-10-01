class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_char_2_count = {}
        t_char_2_count = {}
        for i in range(len(s)):
            s_char_2_count[s[i]] = 1 + s_char_2_count.get(s[i], 0) 
            t_char_2_count[t[i]] = 1 + t_char_2_count.get(t[i], 0) 
        
        for c in s_char_2_count:
            if s_char_2_count[c] != t_char_2_count.get(c, 0):
                return False
        
        return True