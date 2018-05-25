class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        source_len = len(source)
        target_len = len(target)
        if source_len < target_len:
            return -1
        end = source_len - target_len + 1
        for i in range(end):
            if source[i:i + target_len] == target:
                return i
        return -1
