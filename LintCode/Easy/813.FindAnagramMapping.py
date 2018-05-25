class Solution:
    """
    @param A: lists A
    @param B: lists B
    @return: the index mapping
    """

    def anagramMappings(self, A, B):
        # Write your code here
        pos_dict = dict()
        ana_list = []
        for i, b in enumerate(B):
            pos_dict[b] = i

        for a in A:
            ana_list.append(pos_dict[a])

        return ana_list
