from collections import deque

class MyStack:

    def __init__(self):
        self.d = deque()

    def push(self, x: int) -> None:
        self.d.append(x)
        
    def pop(self) -> int:
        counter = 0
        while counter < len(self.d) - 1:
            self.d.append(self.d.popleft())
            counter += 1
        return self.d.popleft()

    def top(self) -> int:
        return self.d[len(self.d) - 1]

    def empty(self) -> bool:
        return True if len(self.d) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()