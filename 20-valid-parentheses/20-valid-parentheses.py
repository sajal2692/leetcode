class Solution:
    def isValid(self, s: str) -> bool:
        close_2_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        open_char_stack = []
        
        for c in s:
            if c in close_2_open:
                if len(open_char_stack) == 0:
                    return False
                open_char = open_char_stack.pop()
                if open_char != close_2_open[c]:
                    return False
            # it is an open paran character
            else:
                open_char_stack.append(c)
        if len(open_char_stack) > 0:
            return False
        return True
                
        