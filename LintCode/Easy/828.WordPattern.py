class Solution:
    """
    @param pattern: a string, denote pattern string
    @param str: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """

    def wordPattern(self, pattern, str):
        # write your code here

        str_list = str.split()
        pattern_dict = dict()

        if len(pattern) != len(str_list):
            return False

        for index, p in enumerate(pattern):
            if p not in pattern_dict:
                if str_list[index] in pattern_dict.values():
                    return False
                pattern_dict[p] = str_list[index]
            elif pattern_dict[p] != str_list[index]:
                return False
            else:
                continue
        return True
