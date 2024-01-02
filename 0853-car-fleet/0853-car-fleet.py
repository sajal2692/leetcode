class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs = sorted(pairs, key=lambda x: x[0], reverse=True)
        stack = []
        
        for pair in pairs:
            position, speed = pair
            time = (target - position) / speed
            stack.append(time)
            # this condition is tricky to get right
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            
            
            