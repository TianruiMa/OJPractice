class Solution:
    """
    @param s: A string
    @return: the length of last word
    """
    def lengthOfLastWord(self, s):
        if s=="" or s is None:
            return 0
        sl = s.split()
        return len(sl[-1])