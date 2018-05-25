class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """

    def gcd(self, a, b):
        # write your code here
        small = min(a, b)
        large = max(a, b)

        # this only works for pos nums
        # if small == large:
        #     return small
        # return self.gcd(large-small,small)
        if small == 0:
            return large
        return self.gcd(small, large % small)