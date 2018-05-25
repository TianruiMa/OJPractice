class Solution:
    """
    @param n: a postive Integer
    @return: if two adjacent bits will always have different values
    """

    def hasAlternatingBits(self, n):
        # Write your code here

        last_dig = None

        while n > 0:
            remd = n % 2
            n = n / 2

            if last_dig == remd:
                return False
            last_dig = remd
        return True