class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = 0, 1

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                # Found a new lower price, so shift buy pointer directly to sell
                buy = sell 
            sell += 1
                

        return max_profit
            
            
        