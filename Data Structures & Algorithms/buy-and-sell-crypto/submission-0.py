class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = prices[0]
        maxval = 0

        for price in prices:
            if price < minval:
                minval = price
                continue
            
            maxval = max(maxval, (price - minval))
        return maxval

        