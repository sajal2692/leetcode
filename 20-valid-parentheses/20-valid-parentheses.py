class Solution:
    def isValid(self, s: str) -> bool:
        close_2_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        # stack to track open parantheses
        open_char_stack = []
        
        for c in s:
            # if c is a closing parantheses
            if c in close_2_open:
                # if there is no open parantheses in the stack, return Fa;se
                if len(open_char_stack) == 0:
                    return False
                # pop the char at the top of the stack
                open_char = open_char_stack.pop()
                # the closing paran does not match opening paren, return False
                if open_char != close_2_open[c]:
                    return False
            # it is an open paran character
            else:
                # add to the top of the stack
                open_char_stack.append(c)
        if len(open_char_stack) > 0:
            return False
        return True
                
        