class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []
        for i, edge in enumerate(edges):
            s, d = edge
            adj[s].append((succProb[i], d))
            adj[d].append((succProb[i], s))
        maxHeap = [(-1, start_node)]
        visited = set()
        while maxHeap:
            p1, d1 = heapq.heappop(maxHeap)
            p1 = -p1
            if d1 == end_node:
                return p1
            if d1 in visited:
                continue
            visited.add(d1)
            for edge in adj[d1]:
                p2, d2 = edge
                if d2 in visited:
                    continue
                heapq.heappush(maxHeap,(-(p1*p2), d2))
        return 0
        