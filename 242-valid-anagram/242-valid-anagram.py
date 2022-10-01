class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_char_2_count = defaultdict(int)
        for c in s:
            s_char_2_count[c] += 1
        
        t_char_2_count = defaultdict(int)
        for c in t:
            t_char_2_count[c] += 1
        
        for c in s_char_2_count:
            if c not in t_char_2_count or s_char_2_count[c] != t_char_2_count[c]:
                return False
        
        return True