from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        ans = j = 0
        for i in range(len(g)):
            while j < len(s) and g[i] > s[j]:
                j += 1
            if j == len(s):
                break
            j += 1
            ans += 1

        return ans

  # 하나만 sort하고 푸는 방법은 없을까?
