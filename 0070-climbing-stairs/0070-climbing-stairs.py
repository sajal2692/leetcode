class Solution(object):

    memo = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1 => 1
        # 2 => 2
        # 3 => c(2) + c(1) => 3
        # 4 => c(3) + c(1) is this ~ c(2) + c(2)? maybe yes?? => 
        # 5 => c(4)
        
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n in self.memo:
            return self.memo[n]
        
        count = self.climbStairs(n-1) + self.climbStairs(n-2) 
        self.memo[n] = count

        return count
        
        