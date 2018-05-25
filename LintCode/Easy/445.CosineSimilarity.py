import math


class Solution:

    def x_product(self, A, B):
        # res = map(lambda (i,a): a*B[i] for i, a in enumerate(A))
        # return sum(res)
        summ = 0.0
        for index, a in enumerate(A):
            summ += a * B[index]

        return summ

    def root_sqr(self, A):
        return math.sqrt(self.x_product(A, A)) * 1.0

    def invalid(self, A):
        for a in A:
            if a != 0:
                return False
        return True

    """
    @param: A: An integer array
    @param: B: An integer array
    @return: Cosine similarity
    """

    def cosineSimilarity(self, A, B):
        # write your code here
        if self.invalid(A) or self.invalid(B):
            return 2.0000
        return self.x_product(A, B) * 1.0 / (self.root_sqr(A) * self.root_sqr(B))
