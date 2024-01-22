class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        res = ""
        
        while p1 < len(word1) and p2 < len(word2):
            res += word1[p1]
            res += word2[p2]
            
            p1 += 1
            p2 += 1
        
        res += word1[p1:] or word2[p2:]
        
        return res