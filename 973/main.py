import heapq
from typing import List

class Solution:
        def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
            heap = []
            for p in points:
                distance = sum(map(lambda x: x ** 2, p))
                heapq.heappush(heap, (distance, p))

            smalllist = heapq.nsmallest(K, heap)

            return list(map(lambda x: x[1], smalllist))
