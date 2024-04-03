from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_time = [0]*n
        call_stack = []
        for log in logs:
            funct_id, cmd, time = list(log.split(':'))
            funct_id, time = int(funct_id), int(time)
            if cmd == "start":
                call_stack.append((funct_id, time))
            else:
                f, t = call_stack.pop()
                if call_stack:
                    exclusive_time[call_stack[-1][0]] -= time-t+1
                exclusive_time[funct_id] += time-t+1

        return exclusive_time
    

## Solution
class Solution:
    def exclusiveTime(self, n: int, logs: List[int]) -> List[int]:
        rslt = [0]*n
        stack = []
        prev = 0
        for log in logs:
            idx, cmd, time = log.split(':')
            idx, time = int(idx), int(time)
            if cmd == "start":
                if stack:
                    rslt[stack[-1]] += time - prev
                stack.append(idx)
                prev = time
            else:
                stack.pop()
                rslt[idx] += time - prev + 1
                prev = time + 1
        
        return rslt
    # prev.. 이전 값 활용!
