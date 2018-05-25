class Solution:
    def insert_to_dict(self, word1, word2, my_dict):
        my_dict[word1].append(word2)
        my_dict[word2].append(word1)

    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """

    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here

        if len(words1) != len(words2):
            return False

        pair_dict = dict()

        for pair in pairs:
            pair_dict[pair[0]] = []
            pair_dict[pair[1]] = []

        for pair in pairs:
            self.insert_to_dict(pair[0], pair[1], pair_dict)

        for index, word1 in enumerate(words1):
            word2 = words2[index]

            if word1 == word2:
                continue
            if pair_dict[word1] is None:
                return False
            if word2 not in pair_dict[word1]:
                return False
        return True
