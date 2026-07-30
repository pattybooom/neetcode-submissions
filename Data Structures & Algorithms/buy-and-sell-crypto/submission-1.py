class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPArr = [0]


        for i in range(1,len(prices)):
            maxp = 0
            for j in range(i-1,-1,-1):
                print(j)
                profit = prices[i] - prices[j]
                if profit > maxp:
                    maxp = profit
            maxPArr.append(maxp)
            print(maxPArr)

        return max(maxPArr)

        