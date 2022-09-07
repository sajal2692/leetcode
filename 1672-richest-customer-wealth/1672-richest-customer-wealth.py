class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum_wealth = - float("inf")
        for i in range(len(accounts)):
            customer_wealth = 0
            for j in range(len(accounts[i])):
                customer_wealth += accounts[i][j]
            maximum_wealth = max(customer_wealth, maximum_wealth)
        return maximum_wealth
                