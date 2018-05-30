import math
import sys
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 3**(floor(log(maxint,3))) = 1162261467  (32-bits)
        return n > 0 and 1162261467 % n == 0


# print 3**(math.floor(math.log((2**31-1),3)))