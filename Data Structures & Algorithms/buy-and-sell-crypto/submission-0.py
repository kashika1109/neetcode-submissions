class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        buyp = 0
        sellp= 1
        while sellp < len(prices):
            if (prices[sellp] > prices[buyp] and prices[sellp] - prices[buyp] > maxp): maxp = prices[sellp] - prices[buyp]
            if (prices[sellp] < prices[buyp]): buyp = sellp
            sellp = sellp + 1
        
        return maxp

