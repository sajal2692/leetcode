import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h is the number of steps (hour)
        # k is the eating speed 
        
        # piles = [3, 6, 7, 11], len = 4,  h = 8, if eating speed is 4
        # steps_needed = piles // 4 (eating_speed) + 1 = [1, 2, 2, 3] ; total = 8
        # 
        
        # [0, 6, 7, 11]
        # [0, 2, 7, 11]
        # [0, 0, 7, 11]
        # [0, 0, 3, 11]
        # [0, 0, 0, 11]
        # [0, 0, 0, 7]
        # [0, 0, 0, 3]
        # [0, 0, 0, 0]
        
        # [30, 11, 23, 4, 20]
        # [0, 11, 23, 4, 20]
        # [0, 0, 23, 4, 20]
        # [0, 0, 0, 4, 20]
        # [0, 0, 0, 0, 0]
        
        
        # optimum solution
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            mid = (l + r) // 2

            total_time_taken = 0
            for p in piles:
                time_taken = math.ceil(p / mid)
                total_time_taken += time_taken # [2, 1, 1, 1, 1]
            if total_time_taken > h:
                l = mid + 1
            elif total_time_taken <= h:
                r = mid - 1
                res = mid
        return res
            
        
        # [1, 30] = (15) 8 > h 5
        # [16, 30] = (23)