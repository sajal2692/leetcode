class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [] # (i, t)
        for i, t in enumerate(temperatures):
            # while the last temperature in the stack is smaller than the current temperature
            while stack and stack[-1][1] <  t:
                # pop the stack
                j, t2 = stack.pop()
                # place the difference between the indices into the answer
                answer[j] = i-j
            stack.append((i, t))
        return answer
                    
            