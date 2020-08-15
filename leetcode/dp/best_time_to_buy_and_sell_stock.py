""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from enum import Enum


class Position(Enum):
    WAITING_FOR_SELL = 1
    WAITING_FOR_BUY = 2



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        total_profit = 0
        pos = Position.WAITING_FOR_BUY
        buy_price = None
        for i in range(len(prices) - 1):
            current_price = prices[i]
            next_price = prices[i+1]
            diff = next_price - current_price
            if pos == Position.WAITING_FOR_BUY and diff > 0:
                # buy now
                buy_price = current_price
                pos = Position.WAITING_FOR_SELL
            elif pos == Position.WAITING_FOR_SELL and diff < 0:
                # sell now
                total_profit += (current_price - buy_price)
                pos = Position.WAITING_FOR_BUY
        
        if pos == Position.WAITING_FOR_SELL:
            # time to sell and take profit
            total_profit += (prices[-1] - buy_price)
        
        return total_profit
            