class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for p in points:
            x, y = p
            distances.append([(x**2)+(y**2), p])
        heapq.heapify(distances)
        res = []
        while k > 0:
            res.append(heapq.heappop(distances)[1])
            k -= 1
        return res