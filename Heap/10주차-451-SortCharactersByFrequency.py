import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        rslt = ''
        counter = collections.Counter(s).most_common()
        for char, freq in counter:
            rslt += char * freq

        return rslt
