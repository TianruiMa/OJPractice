class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0

        J = set(J)

        for s in S:
            if s in J:
                count += 1
        return count
