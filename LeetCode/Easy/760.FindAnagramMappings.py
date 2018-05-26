class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        C = {x: i for i, x in enumerate(B)}
        return list(C[x] for x in A)
