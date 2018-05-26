def invert(list):
    return map(lambda x: invert_number(x), list)


def invert_number(n):
    if n == 0:
        return 1
    else:
        return 0


class Solution(object):

    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        map(lambda a: a.reverse(), A)
        A = map(lambda x: invert(x), A)
        return A
