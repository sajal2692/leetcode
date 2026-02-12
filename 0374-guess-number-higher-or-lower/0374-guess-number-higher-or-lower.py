# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= r:
            pick = (l + r)  // 2
            result = guess(pick)
            if result == 0:
                return pick
            elif result == -1:
                r = pick - 1
            else:
                l = pick + 1


        