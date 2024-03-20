from typing import List

# 1.
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        k_org = k
        for i in range(1, len(nums)):
            k = k_org
            j = i-1
            while j >= 0 and k >= 0 and nums[i]-nums[j] <= k:
                k -= nums[i]-nums[j]
                j -= 1
            ans = max(ans, i-j)
        return ans
    ## Time Limit Exceeded


# 2. 1)max부터 오른쪽, 2)다시 왼쪽 
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_freq = 1
        k_org = k

        for i in range(1, len(nums)):
            k = k_org
            j = i - max_freq + 1
            while j < i and nums[i]-nums[j] <= k:
                k -= nums[i]-nums[j]
                j += 1
            if j != i:
                continue
            j = i - max_freq
            while j >= 0 and nums[i]-nums[j] <= k:
                k -= nums[i]-nums[j]
                j -= 1
            max_freq = i-j

        return max_freq
    ## Time Limit Exceeded

# 3. 슬라이딩 윈도우 - solution
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        ans = 1
        left = right = 0

        while right+1 < len(nums):
            right += 1
            k -= (nums[right]-nums[right-1]) * (right-left)
            while k < 0:
                k += nums[right]-nums[left]
                left += 1
            ans = max(ans, right-left+1) 
        return ans
