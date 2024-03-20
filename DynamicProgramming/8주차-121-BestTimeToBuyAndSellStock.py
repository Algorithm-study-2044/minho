class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        left = right = 0
        while right+1 < len(prices):  # to avoid an index error
            right += 1
            if prices[left] > prices[right]:
                left = right
            else:
                ans = max(ans, prices[right]-prices[left])
        
        return ans
