from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        rslt = trap = 0
        while left < right:
            if height[left] <= height[right]:
                if trap < height[left]: 
                    trap = height[left]
                if height[left+1] < trap:
                    rslt += trap-height[left+1]
                left += 1
            else:
                if trap < height[right]:
                    trap = height[right]
                if height[right-1] < trap:
                    rslt += trap-height[right-1]
                right -= 1
                
        return rslt
    
## Solution 2
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
