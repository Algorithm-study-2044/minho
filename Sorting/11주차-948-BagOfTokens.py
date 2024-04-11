from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens)-1
        score = 0
        while left <= right and power >= tokens[left]:  # Face-up as much as possible
            power -= tokens[left]
            score += 1
            left += 1
        max_score = score   # store the maximum score without using Face-down
        while score > 0 and right >= left:  # Face-down if score is greater than zero
            power += tokens[right]
            score -= 1
            right -= 1
            while left <= right and power >= tokens[left]:  # Face-up as much as possible
                power -= tokens[left]
                score += 1
                left += 1
            max_score = max(max_score, score)   # update the maximum score
        
        return max_score
