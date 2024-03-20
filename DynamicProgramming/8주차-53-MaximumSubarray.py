from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bsum = 0
        for i in range(len(nums)):
            nums[i] += bsum
            bsum = max(0, nums[i])  # 이전 합: 음수면 버린다
        
        return max(nums)
