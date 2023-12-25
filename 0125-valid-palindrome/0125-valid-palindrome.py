class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l, r = 0, len(s) - 1
        # while l < r:
        #     while l < r and not self.isAlphaNum(s[l]):
        #         l += 1
        #     while r > 0 and not self.isAlphaNum(s[r]):
        #         r -= 1
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l += 1
        #     r -= 1
        # return True
    
        l = 0
        r = len(s) - 1
        while l < r:
            if not self.isAlphaNum(s[l]):
                l += 1
            elif not self.isAlphaNum(s[r]):
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
            
    
    def isAlphaNum(self, c):
        return (ord("a") <= ord(c) <= ord("z")) or (ord("A") <= ord(c) <= ord("Z")) or (ord("0") <= ord(c) <= ord("9"))
            