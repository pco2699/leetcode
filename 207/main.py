from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        inbound = defaultdict(int)
        for p in prerequisites:
            curr, prev = p[0], p[1]
            adjList[prev].append(curr)
            inbound[curr] += 1

        res = deque()
        queue = deque()
        for n in range(numCourses):
            if inbound[n] == 0:
                queue.append(n)

        while queue:
            curr = queue.popleft()
            res.append(curr)
            for adj in adjList[curr]:
                inbound[adj] -= 1
                if inbound[adj] == 0:
                    queue.append(adj)

        return len(res) == numCourses

