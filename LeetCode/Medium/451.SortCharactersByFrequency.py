class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        str_set = set(s)
        char_dict = dict()
        sorted_str = ""

        for c in str_set:
            n = s.count(c)
            char_dict[c] = n

        k = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

        for key, value in k:
            sorted_str += (key * value)

        return sorted_str
