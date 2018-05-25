
class Solution:
    """
    @param g: children's greed factor
    @param s: cookie's size
    @return: the maximum number
    """

    def findContentChildren(self, g, s):
        # Write your code here
        g.sort(reverse=True)
        s.sort(reverse=True)

        givenout_cookie = 0
        for c in g:
            if givenout_cookie >= len(s):
                return givenout_cookie
            if s[givenout_cookie] >= c:
                givenout_cookie += 1
        return givenout_cookie
