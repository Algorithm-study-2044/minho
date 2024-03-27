from typing import List
import itertools, random, bisect

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        target = random.randint(0, self.prefix[-1]-1)
        return bisect.bisect_right(range(len(self.prefix)), target, key=lambda m: self.prefix[m])


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
