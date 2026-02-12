# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
# [0, 0, 0, 1, 1, 1, 1, 1]
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        first_bad = None
        while l <= r:
            guess = (l + r) // 2
            is_bad = isBadVersion(guess)
            if is_bad:
                first_bad = guess
                r = guess - 1
            else:
                l = guess + 1
        return first_bad
