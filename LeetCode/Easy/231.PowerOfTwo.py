class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        # bin_str = bin(n)[2:]
        # return bin_str[0] and bin_str.count('1') == 1

        return (n &(n-1)) == 0