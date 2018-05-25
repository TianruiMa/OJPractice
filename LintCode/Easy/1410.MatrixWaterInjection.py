class Solution:

    def try_flow(self, matrix, r, c, last_val):
        # bound = len(matrix)
        curr_val = matrix[r][c]
        # if r < 0 or r >= rbound or c < 0 or c >=cbound:
        #     return False

        if curr_val < last_val:
            return self.ans(matrix, r, c)
        else:
            return False

    def ans(self, matrix, R, C):
        bound = len(matrix)
        curr_val = matrix[R][C]

        if R == 0 or R == bound - 1 or C == 0 or C == bound - 1:
            return True
        else:
            return self.try_flow(matrix, R, C - 1, curr_val) or \
                   self.try_flow(matrix, R, C + 1, curr_val) or \
                   self.try_flow(matrix, R - 1, C,  curr_val) or \
                   self.try_flow(matrix, R + 1, C, curr_val)

    """
    @param matrix: the height matrix
    @param R: the row of (R,C)
    @param C: the columns of (R,C)
    @return: Whether the water can flow outside
    """

    def waterInjection(self, matrix, R, C):
        # Write your code here
        if self.ans(matrix, R, C):
            return "YES"
        else:
            return "NO"
