from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
        # Can only buy and sell once
        # Find the maximum non-negative difference where the subtracted number follows the subtraction
        lowest_buying_price = 1e4
        max_profit = 0       # O(1) space cost

        for price in prices:
            max_profit = max(max_profit, price - lowest_buying_price)
            lowest_buying_price = min(lowest_buying_price, price)  # could only be sold in the future

        return max_profit