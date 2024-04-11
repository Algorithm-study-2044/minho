import collections

class Solution:
    def minOperations(self, n: int) -> int:
        memo = collections.defaultdict(int)
        def division(divisor):
            if memo[divisor]:
                return memo[divisor]

            dividend = 1
            while dividend < divisor:
                dividend *= 2
            if dividend == divisor:
                return 1

            d1 = dividend - divisor
            d2 = divisor % (dividend//2)

            out = min(division(d1), division(d2)) + 1
            memo[divisor] = out
            return out

        return division(n)
