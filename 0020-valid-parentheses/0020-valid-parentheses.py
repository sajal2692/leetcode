class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s:
            if c not in paren:
                stack.append(c)
            else:
                if not stack or stack.pop() != paren[c]:
                    return False
        if stack:
            return False
        return True
                
            