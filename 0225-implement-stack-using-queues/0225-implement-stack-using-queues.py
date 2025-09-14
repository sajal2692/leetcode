from collections import deque

class MyStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()