"""
Time complexity: O(n)
Space complexity: O(1)
Thought process:
- The optimized solution is to iterate through the list, and keep changing the buying price to the smallest. Then, repeatedly calculate the profit, and get the maximum one.
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize result variable, and a buy variable that hold the price when buy
        result = 0
        buy = prices[0]
        # Iterate through the prices array, and change buy to an element smaller than the previous one
        for sell in prices:
            if sell < buy:
                buy = sell
                continue
            else:
                # Repeatedly calculate the profit, and compare to the currrent one
                result = max(result, sell - buy)
        return result