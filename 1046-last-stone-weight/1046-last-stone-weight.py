class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if x==y:
                continue
            new_stone = y - x
            heapq.heappush(max_heap, -new_stone)
        return -max_heap[0] if max_heap else 0
        