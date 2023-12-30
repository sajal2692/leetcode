class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        
        def backtrack(countL, countR):
            if countL == countR == n:
                result.append("".join(stack))
                return
            if countL < n:
                stack.append("(")
                backtrack(countL+1, countR)
                stack.pop()
            if countR < countL:
                stack.append(")")
                backtrack(countL, countR+1)
                stack.pop()
        
        backtrack(0,0)
        return result