from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = sum(nums)

        for i in range(len(nums)-2):
            total -= nums[i]
            if nums[i] < total:
                return total+nums[i]
        return -1
    
