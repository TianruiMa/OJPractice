class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """

    def isHappy(self, n):
        # write your code here
        if n == 1:
            return True
        if n == 4:
            return False

        res = 0
        for t in str(n):
            res += int(t) ** 2

        return self.isHappy(res)
