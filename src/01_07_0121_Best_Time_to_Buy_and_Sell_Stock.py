"""
# Best Time to Buy and Sell Stock

- **ID:** 121
- **Difficulty:** EASY
- **Topic Tags:** Array, Dynamic Programming
- **Link:** [LeetCode Problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minLeft = prices[0]
        res = 0
        for x in prices:
            if minLeft > x:
                minLeft = x
            res = max(res, x - minLeft)
        return res

"""
because we know the future in the price, this question is intented to calculate the ideal biggest profit
"""