class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxp = 0


        for i in range(1,len(prices)):
            
            profit = prices[i] - minPrice
            if profit > maxp:
                maxp = profit
            if prices[i] < minPrice:
                minPrice = prices[i]
           
    

        return maxp

        