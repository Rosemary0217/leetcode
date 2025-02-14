from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
        On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
        """
        total_profit = 0
        min_buying_price, max_selling_price = prices[0], -1
        share = 0

        for price in prices:
            if share == 0:     # holds no share, can only buy
                if price < min_buying_price:
                    min_buying_price = price
                elif price > min_buying_price:
                    share += 1   # buy when the price comes at a local minimum
            if share == 1:    # holds one share, can only sell
                if price > max_selling_price:
                    max_selling_price = price  # keep watching on
                if price < max_selling_price:   # price went down later on
                    total_profit += max_selling_price - min_buying_price   # sell at local maximum
                    share -= 1
                    max_selling_price = -1
                    min_buying_price = price
                
            
        if share == 1:
            total_profit += max(0, max_selling_price - min_buying_price)

        return total_profit
    
# sol = Solution()
# prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
# prices = [2,1,2,0,1]
# print(sol.maxProfit(prices))