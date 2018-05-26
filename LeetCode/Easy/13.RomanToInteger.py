class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total = 0
        s_len = len(s)
        for i in xrange(s_len - 1):
            curr_val = roman_dict[s[i]]
            next_val = roman_dict[s[i + 1]]
            if curr_val < next_val:
                total -= curr_val
            else:
                total += curr_val
        total += roman_dict[s[-1]]
        return total