class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.end = "**"

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        level = self.trie
        for c in word:
            if c in level:
                level = level[c]
            else:
                level[c] = {}
                level = level[c]
        level[self.end] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        level = self.trie
        for c in word:
            if c in level:
                level = level[c]
            else:
                return False
        return self.end in level

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        level = self.trie
        for c in prefix:
            if c in level:
                level = level[c]
            else:
                return False
        return True



a = [1,2,3,4,5]
print a.rfind(1)