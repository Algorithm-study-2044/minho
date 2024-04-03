from typing import List

## if nums[i] > 0:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def radix_sort(nums):
            n = len(nums)
            max_val = max(nums)
            radix = 1
            while radix <= max_val:
                radix *= 10
            count = [0]*10
            bucket = [0]*n
            
            i = 1
            while i < radix:
                for j in range(n):
                    count[(nums[j]//i)%10] += 1
                for j in range(1, 10):
                    count[j] += count[j-1]
                for j in range(n-1, -1, -1):
                    bucket[count[(nums[j]//i)%10]-1] = nums[j]
                    count[(nums[j]//i)%10] -= 1
                for j in range(n):
                    nums[j] = bucket[j]
                count = [0]*10
                i *= 10
            return nums

        if nums == []:
            return 0

        nums = radix_sort(nums)
        max_len, length = 0, 1
        for i in range(1, len(nums)):
            if nums[i]-1 == nums[i-1]:
                length += 1
            else:
                max_len = max(max_len, length)
                length = 1
        max_len = max(max_len, length)

        return max_len
    
## O(nlogn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums.sort()
        longest, length = 0, 1
        for i in range(1, len(nums)):
            if nums[i]-1 == nums[i-1]:
                length += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                longest = max(longest, length)
                length = 1
        longest = max(longest, length)
            
        return longest
    

## Solution 1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num-1 in num_set:
                continue
            length = 1
            while num+length in num_set:
                length += 1
            longest = max(longest, length)
        
        return longest
    
## Solution 2
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        while nums:
            n = nums.pop()
            m = n - 1
            o = n + 1
            while m in nums:
                nums.remove(m)
                m -= 1
            while o in nums:
                nums.remove(o)
                o += 1
            res = max(res, o - m - 1)
        return res
    # set in python:
        # add, pop, remove, in: O(1)
