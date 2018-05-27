class Solution(object):
    # def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # length = len(s)
        # res = ""
        # if numRows <= 1: return res
        # for level in range(numRows):
        #     for j in range(level, length, (numRows - 1) * 2):
        #         res += s[j]
        #         further = j + (numRows - 1 - level) * 2
        #         if further < length and level != 0 and level != numRows-1:
        #             res += s[further]
        #     print ("")
        # return res

        def convert(self, s, numRows):
            """
            :type s: str
            :type numRows: int
            :rtype: str
            """

            if numRows <= 1: return s
            ans = [''] * numRows
            level = 0
            direction = 1
            for c in s:
                ans[level] += c
                if level == 0: direction = 1
                elif level == numRows - 1: direction = -1
                level += direction
            return ''.join(ans)

