class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxInt = 2**31-1
        minInt = -1 * 2**31
        if x < 0:
            y  = -1 * int(str(-x)[::-1])
        else:
            y  = int(str(x)[::-1])
        if y > maxInt or y < minInt:
            return 0
        return y


ma = dict()
print ma['c']