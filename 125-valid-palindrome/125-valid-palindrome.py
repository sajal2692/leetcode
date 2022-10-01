class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = "".join([c.lower() for c in s if c.isalnum()])
        reversed_s = filtered_s[::-1]
        return filtered_s == reversed_s