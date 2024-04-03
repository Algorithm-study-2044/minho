from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        i = 0
        while i < len(heights)-1:
            if heights[i] < heights[i+1]:
                heapq.heappush(heap, heights[i+1]-heights[i])
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                    if bricks < 0:
                        break
            i += 1

        return i
