class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = prices[0]

        for price in prices:
            minPrice = min(price, minPrice)
            profit = price - minPrice
            maxProfit = max(profit, maxProfit)

        return maxProfit


obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))
print(obj.maxProfit([7, 6, 4, 3, 1]))
