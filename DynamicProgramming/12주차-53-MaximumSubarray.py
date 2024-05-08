from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        
        return max_sum
    

## Solution 2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)
        if max_sum < 0:
            return max_sum

        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum < 0:
                cur_sum = 0
            elif cur_sum > max_sum:
                max_sum = cur_sum
        
        return max_sum
