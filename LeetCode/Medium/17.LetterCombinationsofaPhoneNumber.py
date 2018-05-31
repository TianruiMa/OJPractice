import itertools


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []

        dial_dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        last = list(dial_dict[digits[0]])
        for d in digits[1:]:
            last = map(lambda (x, y): x + y, list(itertools.product(last, dial_dict[d])))

        return last
