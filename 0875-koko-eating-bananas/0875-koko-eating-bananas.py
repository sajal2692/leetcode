import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h is the number of steps (hour)
        # k is the eating speed 
        
        # piles = [3, 6, 7, 11], len = 4,  h = 8, if eating speed is 4
        # steps_needed = piles // 4 (eating_speed) + 1 = [1, 2, 2, 3] ; total = 8

        # optimum solution
        l, r = 1, max(piles)
        res = 0 # need this to keep track of edge case where the last iteration of the binary search may lead to a ->
        # <- mid point with more time taken than needed
        while l <= r:
            mid = (l + r) // 2

            total_time_taken = 0
            for p in piles:
                time_taken = math.ceil(p / mid)
                total_time_taken += time_taken 
            if total_time_taken > h:
                l = mid + 1
            elif total_time_taken <= h:
                r = mid - 1
                # only assign the mid point to the result if the total time taken is <= the max limit (h)
                res = mid
        return res
            
        
        # [1, 30] = (15) 8 > h 5
        # [16, 30] = (23)