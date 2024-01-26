class Solution:
    def fib(self, n: int) -> int:
        
        # base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # recursive case
        return self.fib(n-1) + self.fib(n-2)
        
        