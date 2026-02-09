class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0 
        current_price = prices[0]

        for i in prices[1:]:
            if i < current_price:
                current_price = i 

            profit = max(profit, i-current_price)

        return profit


