class Solution:
    def isValid(self, s: str) -> bool:
        close_2_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack = []
        
        for c in s:
            if c in close_2_open:
                if stack and stack[-1] == close_2_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        return False
                
                
                
            