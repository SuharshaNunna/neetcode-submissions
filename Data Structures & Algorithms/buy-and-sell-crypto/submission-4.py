class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #order matters
        #want to buy at min, sell at max 
        # if next number is less than prev no point in buying 
        # two pointers : one to buy and one to sell
        # both start at left most incriment buy if nect number is less,
        # have a sell if current number is higher than buy or higher than sell
        # buy needs to come before sell
        # profit = buy- sell
        # buy and sell is the th day 
        buy, sell = 0, 1
        maxP = 0
        #while the sell day is within bounds 
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
            else:
                buy = sell
            sell += 1
        return maxP
        