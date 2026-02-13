class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            speed = (l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            if hours > h:
                l = speed + 1
            else:
                r = speed - 1
        return l
        
