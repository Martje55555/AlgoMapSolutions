# Time Complexity - O(n) | Space Complexity - O(1)

class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0

        for price in prices:
            if buy > price:
                buy = price
            if profit < price - buy:
                profit = price - buy
        return profit