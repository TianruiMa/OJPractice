class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """

    def validWordSquare(self, words):
        # Write your code here

        # bound = len(words)
        #
        # for x in range(bound):
        #     rword = words[x][x:]
        #     cword = "".join(w[x] for w in words)[x:]
        #     if rword != cword:
        #         return False
        # return True

        for r in range(len(words)-1):
            for c in range(r+1,len(words)):
                if words[r][c] != words[c][r]:
                    return False
        return True
