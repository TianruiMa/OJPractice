class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        str_n = str(number)
        str_n = str_n[::-1]
        return int(str_n)
