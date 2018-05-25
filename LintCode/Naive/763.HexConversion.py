def convert_to_char(i):
    if i < 10:
        return str(i)
    else:
        return str(unichr(i + 55))


class Solution:
    """
    @param n: a decimal number
    @param k: a Integer represent base-k
    @return: a base-k number
    """

    def hexConversion(self, n, k):
        # write your code here
        if n == 0:
            return "0"
        str = ""
        while n != 0:
            r = n % k
            str = convert_to_char(r) + str
            n /= k
        return str


print Solution().hexConversion(5, 2)
