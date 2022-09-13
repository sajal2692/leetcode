class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use a two pointer (l,r) algo to solve this
        l, r = 0, 1
        max_profit = 0
        # while right pointer is in bounds
        while r < len(prices):
            # if transaction is profitable
            if prices[l] < prices[r]: # price on left is lower
                profit = prices[r] - prices[l] # calculate profit
                max_profit = max(max_profit, profit) # update max_profit if required
            else:
                l = r # move l to r as new low price was found
            r += 1 # increment r as we can only check prices after the current r
        return max_profit
                