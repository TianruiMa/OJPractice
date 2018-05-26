class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # max_str = ""
        # longest = 0
        # res = ""
        # index = 0
        # while index < len(s):
        #     pos = res.find(s[index])
        #     if pos == -1:
        #         res += s[index]
        #         # max_str = max_str if len(max_str)>=len(res) else res
        #         longest = max(len(res),longest)
        #     else:
        #         res = res[pos+1:]+s[index]
        #     index += 1
        # return longest

        charMap = dict()
        ansIndex = 0
        longest = 0
        i = 0
        for c in s:
            if c in charMap:
                if charMap[c] > ansIndex:
                    ansIndex = charMap[c] + 1
            charMap[c] = i
            subLenght = i - ansIndex + 1

            if subLenght > longest:
                longest = subLenght
            i = i + 1
        return longest


Solution().lengthOfLongestSubstring("abba")