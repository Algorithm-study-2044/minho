from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rslt = [0]*len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i, _ = stack.pop()
                rslt[i] = idx-i
            stack.append((idx, temp))

        return rslt
    
## improved Solution
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        rslt = [0]*len(temp)
        stack = []
        for idx in range(len(temp)):
            while stack and temp[stack[-1]] < temp[idx]:
                i = stack.pop()
                rslt[i] = idx - i
            stack.append(idx)

        return rslt
    # no need to store temp in the stack..
