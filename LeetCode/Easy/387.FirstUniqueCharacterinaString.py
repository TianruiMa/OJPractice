class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        # for i,c in enumerate(s):
        #     if(s.rfind(c) == s.find(c)):
        #         return i
        # return -1

        minIdx = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            curIdx = s.find(c)
            if curIdx != -1 and curIdx == s.rfind(c):
                minIdx = min(minIdx, curIdx)
        return minIdx if minIdx != len(s) else -1