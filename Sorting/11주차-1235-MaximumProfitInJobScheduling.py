from typing import List
import bisect

## Time limit exceeded
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        idx = sorted([i for i in range(len(endTime))], key=lambda x: endTime[x])

        for i in range(1, len(idx)):
            for j in range(i-1, -1, -1):
                if endTime[idx[j]] <= startTime[idx[i]]:
                    profit[idx[i]] += profit[idx[j]]
                    break
            profit[idx[i]] = max(profit[idx[i]], profit[idx[i-1]])
        
        return profit[idx[-1]]
    
## binary search added
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        idx = sorted([i for i in range(len(endTime))], key=lambda x: endTime[x])
        for i in range(1, len(idx)):
            left, right = 0, i-1
            while left < right:
                mid = left + (right-left+1)//2
                if endTime[idx[mid]] < startTime[idx[i]]:
                    left = mid
                elif endTime[idx[mid]] > startTime[idx[i]]:
                    right = mid-1
                else:
                    left = mid
                    break
            if endTime[idx[left+1]] <= startTime[idx[i]]:
                profit[idx[i]] += profit[idx[left+1]]
            elif endTime[idx[left]] <= startTime[idx[i]]:
                profit[idx[i]] += profit[idx[left]]
            profit[idx[i]] = max(profit[idx[i]], profit[idx[i-1]])
        
        return profit[idx[-1]]
    

## Solution
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        sorted_endTime = [x[1] for x in jobs]
        n = len(jobs)

        dp = [0]*n
        dp[0] = jobs[0][2]

        for i in range(1, n):
            cur_start, _, cur_profit = jobs[i]
            j = bisect.bisect_right(sorted_endTime, cur_start) - 1
            if j >= 0:
                cur_profit += dp[j]
            dp[i] = max(cur_profit, dp[i-1])
        
        return dp[-1]
