from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        left = right = 0  # 1(<-left) 1 1 1 2(<-right)...
        while right < len(nums):
            while right < len(nums) and nums[left] == nums[right]:
                right += 1
            if right - left == 1: 
                return -1
            q, r = divmod(right-left, 3)
            if r == 0:  # 3의 배수
                ans += q
            else:       #q three + 1 two or q-1 three + 2 two
                ans += q+1
            left = right

        return ans
