class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        [10,8,7,5,2]
                  ^
            l

         lowest = 2

         profit = 0
        """

        min_price = float("inf")
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

        