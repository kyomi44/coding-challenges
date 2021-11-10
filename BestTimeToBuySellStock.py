class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        
        if prices:
            mini = prices[0]
        else:
            return ans
        
        for i in range(1, len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            else:
                ans += (prices[i] - mini)
                mini = prices[i]
                
        return ans