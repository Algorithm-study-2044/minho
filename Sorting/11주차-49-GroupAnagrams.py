from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = collections.defaultdict(list)
        for str in strs:
            group[''.join(sorted(str))].append(str)
        return group.values()
