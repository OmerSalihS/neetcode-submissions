class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        dif=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                dif=max(dif,prices[j]-prices[i])
        return dif
        