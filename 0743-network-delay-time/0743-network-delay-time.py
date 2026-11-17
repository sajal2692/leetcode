class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        for time in times:
            u, v, w = time
            adj[u].append((w,v))
        
        minTime = 0
        minHeap = [(0, k)]
        visited = set()

        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            if v1 in visited:
                continue
            visited.add(v1)
            minTime = max(minTime, w1)
            edges = adj[v1]
            for edge in edges:
                w2, v2 = edge
                if v2 not in visited:
                    heapq.heappush(minHeap, (w2+w1, v2))
        
        return minTime if len(visited) == n else -1

