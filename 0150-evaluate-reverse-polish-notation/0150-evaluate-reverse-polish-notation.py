class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
                continue
            a = stack.pop()
            b = stack.pop()
            if t == "+":
                stack.append(b+a)
            elif t == "-":
                stack.append(b-a)
            elif t == "*":
                stack.append(b * a)
            elif t == "/":
                stack.append(int(b/a))
        return stack.pop()