import os
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        def longestCommonPrefix(self, strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            # prefix = ""
            # if strs is not None and len(strs) > 0:
            #     prefix = strs[0]
            #     pLen = len(prefix)
            #     for strToCompare in strs[1:]:
            #         while (pLen > 0):
            #             if prefix[:pLen] != strToCompare[:pLen]:
            #                 pLen -= 1
            #             else: break
            #         if pLen == 0: break
            #     prefix = prefix[:pLen]
            # return prefix

        return os.path.commonprefix(strs)