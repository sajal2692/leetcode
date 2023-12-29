class Solution:
    def trap(self, height: List[int]) -> int:
        # multi-pass solution
        n = len(height)
        maxLs = [0] * n
        maxRs = [0] * n
        amount = 0
        
        
        # forward pass to calculate maxLs
        for i in range(1, n, 1):
            maxLs[i] = max(height[i-1], maxLs[i-1])
        
        # backward pass to calculate maxRs
        for i in range(n-1, -1, -1):
            if i == n - 1:
                continue
            maxRs[i] = max(height[i+1], maxRs[i+1])
        
        print(maxLs)
        print(maxRs)
        for i, h in enumerate(height):
            a = min(maxLs[i], maxRs[i]) - h
            amount += max(0, a)
            
        return amount
        
        