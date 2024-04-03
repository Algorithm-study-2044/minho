from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        arr.sort()
        cnt_dict = {}
        for i in range(len(arr)):
            cnt_dict[arr[i]] = 1
            for j in range(0, i):
                k, r = divmod(arr[i], arr[j])
                if r == 0 and k in cnt_dict:
                    cnt_dict[arr[i]] += cnt_dict[arr[j]] * cnt_dict[k]

        rslt = 0
        for num in cnt_dict.values():
            rslt += num
        
        return rslt % mod
    

## Solution
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        arr.sort()
        dp = [1] * len(arr)
        num_to_idx = {n: i for i, n in enumerate(arr)}
        for i, root in enumerate(arr):
            for j in range(i):
                if root % arr[j] == 0:
                    right = root // arr[j]
                    if right in num_to_idx:
                        dp[i] += dp[j] * dp[num_to_idx[right]]
                        dp[i] % mod

        return sum(dp) % mod
    # num_to_idx dictionary..!
