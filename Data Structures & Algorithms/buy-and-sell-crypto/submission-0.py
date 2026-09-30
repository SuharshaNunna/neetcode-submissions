class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers, one keeping track of the buy ( buy at the lowest price), one keeping 
        # track of the sell ( highest price)
        # buy should always be before the sell 

        # iterate though a subarray and only store the profit if it is higher than the last 
        maxprof= 0
        buy = 0 
        sell= 1
        while sell < len(prices):
            if prices[buy] < prices[sell]: 
                prof = prices[sell] - prices[buy] 
                maxprof = max(prof,maxprof) 
            else:
                buy = sell
            sell+=1 

        return maxprof

