class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBef = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < minBef:
                minBef = prices[i]
            else:
                ans = max(prices[i]-minBef, ans)

        return ans