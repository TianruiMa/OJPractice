class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_dict = {'{':'}', '[':']', '(':')'}

        my_stack = []
        for p in s:
            if p in p_dict:
                my_stack.append(p_dict[p])
            elif len(my_stack) == 0 or p != my_stack[-1]:
                return False
            else:
                my_stack.pop()
        return True